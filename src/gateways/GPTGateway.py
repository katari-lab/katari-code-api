from typing import List
import openai
import os
from openai import OpenAI
import logging

LOGGER = logging.getLogger(__name__)


class GPTGateway:
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI()

    def get_assistant(self, assistant_id):
        return self.client.beta.assistants.retrieve(assistant_id)

    def create_assistant(
        self,
        name: str,
        instructions: str,
        response_format: str = "text",
        temperature: float = 1.0,
        top_p: float = 1.0,
    ):
        assistant = self.client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=[],
            response_format={"type": response_format},
            temperature=temperature,
            top_p=top_p,
            model="gpt-4o",
        )
        return assistant

    def update_assistant_instructions(self, assistant_id, instructions):
        return self.client.beta.assistants.update(
            assistant_id, instructions=instructions, tools=[{"type": "file_search"}]
        )

    def update_vector_store_ids(self, assistant_id, vector_store_ids: List):
        return self.client.beta.assistants.update(
            assistant_id,
            tool_resources={"file_search": {"vector_store_ids": vector_store_ids}},
        )

    def update_assistant_temperature(self, assistant_id, temperature: float):
        return self.client.beta.assistants.update(assistant_id, temperature=temperature)

    def update_assistant_response_format(self, assistant_id, response_format):
        return self.client.beta.assistants.update(
            assistant_id, response_format=response_format
        )

    def update_assistant_top_p(self, assistant_id, top_p: float):
        return self.client.beta.assistants.update(assistant_id, top_p=top_p)

    def create_thread(self):
        thread = self.client.beta.threads.create()
        return thread

    def create_user_message(self, thread_id, content: str):
        return self.client.beta.threads.messages.create(
            thread_id=thread_id, role="user", content=content
        )

    def create_and_poll(self, thread_id, assistant_id, instructions=""):
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=assistant_id,
            instructions=instructions,
        )
        if run.status == "completed":
            messages = self.client.beta.threads.messages.list(thread_id=thread_id)
            return messages
        else:
            raise ValueError(run.status)

    def describe_vector_store(self, name: str):
        # vector_store = self.client.beta.vector_stores.retrieve(vector_store_id=name)
        for vector_store in self.client.beta.vector_stores.list():
            print(vector_store)
        # return vector_store

    def list_vector_stores(self):
        result = []
        for vector_store in self.client.beta.vector_stores.list():
            result.append(vector_store)
        return result

    def upload_files_to_vector_store(self, name: str, file_paths):
        vector_store = self.client.beta.vector_stores.create(name=name)
        file_streams = [open(path, "rb") for path in file_paths]

        file_batch = self.client.beta.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store.id, files=file_streams
        )

        LOGGER.info(file_batch.status)
        LOGGER.info(file_batch.file_counts)
        LOGGER.info(vector_store.id)
        return vector_store.id

    def ask_llm(
        self, system: str, prompt: str, model="gpt-4o", temperature=0.8, max_tokens=2000
    ):
        try:
            chat_completion = self.client.chat.completions.create(
                temperature=temperature,
                max_tokens=max_tokens,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                model=model,
            )
            return chat_completion
        except Exception as ex:
            raise ValueError(f"Error with model {model}") from ex
