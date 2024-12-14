import unittest
import io
import numpy as np
from ..common import load_ini_and_set_env
from src.components.TranscriptComponent import TranscriptComponent
import simpleaudio as sa


class TestTranscriptComponent(unittest.TestCase):

    def setUp(self):
        load_ini_and_set_env()
        super().setUp()

    def test_get_features(self):
        audio_file_path = "./dataset/editor delete line.wav"
        component = TranscriptComponent()
        features = component.get_audio_features(audio_file_path)
        self.assertTrue(features)
        for f in features:
            print(type(f))

    def test_audio_transcript(self):
        component = TranscriptComponent()
        audio_file_path = "./dataset/editor delete line.wav"
        with open(audio_file_path, "rb") as f:
            audio = f.read()
            transcript = component.transcript_from_wav_bytes(audio, "audio.wav")
            self.assertTrue(transcript)

    def test_audio_transcript_raw(self):
        component = TranscriptComponent()
        audio_file_path = "./dataset/newline.pcm"
        with open(audio_file_path, "rb") as f:
            audio = f.read()
            transcript = component.transcript_from_raw_bytes(audio)
            self.assertTrue(transcript)

    def test_reduce_silence(self):
        component = TranscriptComponent()
        audio_file_path = "./dataset/aa.pcm"
        with open(audio_file_path, "rb") as f:
            wav_bytes = component.convert_from_raw_to_wav(f.read())
            wav_bytes = component.convert_to_16000(wav_bytes)
            wav_bytes = component.remove_silence(wav_bytes)
            transcript = component.transcript_from_wav_bytes(wav_bytes)
            self.assertTrue(transcript)

            try:
                audio_stream = sa.WaveObject.from_wave_file(io.BytesIO(wav_bytes))
                play_obj = audio_stream.play()
                play_obj.wait_done()  # Wait until playback is finished
            except Exception as e:
                print(f"Error playing audio: {e}")

    def test_similar_sentences(self):
        component = TranscriptComponent()
        a_file = "./dataset/define function _____.wav"
        a_features = component.get_audio_features(a_file)
        b_file = "./dataset/define function__.wav"
        # b_file = "./dataset/define function _____.wav"
        b_features = component.get_audio_features(b_file)
        for a, b in zip(a_features, b_features):
            min_length = min(a.shape[1], b.shape[1])
            result = np.allclose(a[:, :min_length], b[:, :min_length])
            print(result)
