from openai import OpenAI
import mimetypes


class WhisperGateway:

    def __init__(self):
        self.client = OpenAI()

    def transcribe_audio(self, audio_file_path):
        with open(audio_file_path, "rb") as audio_file:
            transcription = self.transcript_from_bytes(audio_file)
            return transcription

    def transcript_from_bytes(self, audio: bytes, filename: str) -> str:
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type not in [
            "audio/flac",
            "audio/m4a",
            "audio/mp3",
            "audio/mp4",
            "audio/mpeg",
            "audio/mpga",
            "audio/ogg",
            "audio/wav",
            "audio/webm",
        ]:
            raise ValueError(
                f"Unsupported file format for {filename}. Supported formats: flac, m4a, mp3, mp4, "
                f"mpeg, mpga, oga, ogg, wav, webm"
            )
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1", file=(filename, audio, mime_type)
        )
        return transcription.text
