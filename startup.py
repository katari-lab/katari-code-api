from fastapi import FastAPI, File, UploadFile, Request
import soundfile as sf
from io import BytesIO
import os
import logging
from src.components.CodeComponent import CodeComponent
from src.components.TestingComponent import TestingComponent
from contextlib import asynccontextmanager
import configparser
from starlette.responses import PlainTextResponse
from src.components.TranscriptComponent import TranscriptComponent
import logging
SAVE_DIR = "./uploaded_files"

LOGGER = logging.getLogger(__name__)

def load_configurations(file_path: str):
    config = configparser.ConfigParser()
    config.read(file_path)

    if not os.path.exists(os.path.abspath(file_path)):
        raise ValueError(f"Configuration file not found: {os.path.abspath(file_path)}")

    for key, value in config["DEFAULT"].items():
        os.environ[key] = value


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("App initialization")
    yield


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    @app.get("/")
    async def read_root(request: Request):
        body_text = (await request.body()).decode("utf-8")
        logging.info(body_text)
        component = CodeComponent()
        response = component.code(body_text)
        return {"content": response}

    @app.post("/code")
    async def post_code(request: Request):
        filename = request.query_params.get("filename") 
        LOGGER.info("lint code %s", filename)
        body_text = (await request.body()).decode("utf-8")        
        component = CodeComponent()
        response = component.lint_code(filename, body_text)
        return PlainTextResponse(content=response)
    
    @app.post("/test")
    async def post_test(request: Request):
        filename = request.query_params.get("filename") 
        LOGGER.info("lint code %s", filename)
        body_text = (await request.body()).decode("utf-8")        
        component = TestingComponent()
        response = component.create_unit_test(filename, body_text)
        return PlainTextResponse(content=response)

    @app.post("/commands/transcript")
    async def post_audio(file: UploadFile = File(...)):
        audio_bytes = await file.read()
        file_path = os.path.join(SAVE_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(audio_bytes)
        component = TranscriptComponent()
        message = component.transcript_from_raw_bytes(audio_bytes, file.filename)
        result = {
            "filename": file.filename,
            "content_type": file.content_type,
            "message": message,
            "file_size": len(audio_bytes),
        }
        return result

    return app


current_directory = os.path.dirname(os.path.abspath(__file__))
ini_file_path = os.path.join(current_directory, "startup.ini")

load_configurations(ini_file_path)
setup_logging()
app = create_app()

# Run: uvicorn startup:app --host 0.0.0.0 --port 8000 --reload
