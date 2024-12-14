import unittest
from src.gateways.WhisperGateway import WhisperGateway
from ..common import load_ini_and_set_env


class TestWhisperGateway(unittest.TestCase):
    def setUp(self):
        load_ini_and_set_env()
        super().setUp()

    def test_transcript(self):
        audio_file_path = "./dataset/editor delete line.wav"
        whisper = WhisperGateway()
        transcribed_text = whisper.transcribe_audio(audio_file_path)
        self.assertTrue(transcribed_text)
        print(transcribed_text)


if __name__ == "__main__":
    unittest.main()
