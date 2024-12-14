import librosa
import io
import wave
from pydub import AudioSegment
import soundfile as sf
from io import BytesIO
from pydub.silence import detect_nonsilent
from ..gateways.WhisperGateway import WhisperGateway
import logging

LOGGER = logging.getLogger(__name__)


class TranscriptComponent:
    def __init__(self):
        self.transcript_gateway = WhisperGateway()

    def get_audio_features(self, audio_file_path):
        audio_data, sample_rate = librosa.load(audio_file_path)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(audio_data)
        spectral_centroid = librosa.feature.spectral_centroid(
            y=audio_data, sr=sample_rate
        )
        mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
        return [zero_crossing_rate, spectral_centroid, mfccs]

    def transcript_from_wav_bytes(self, audio_bytes: bytes):
        return self.transcript_gateway.transcript_from_bytes(audio_bytes, "audio.wav")

    def transcript_from_raw_bytes(self, audio_bytes: bytes, raw_file_name: str):
        LOGGER.info("transcript start %s ", raw_file_name)
        wav_bytes = self.convert_from_raw_to_wav(audio_bytes)
        wav_bytes = self.convert_to_16000(wav_bytes)
        # wav_bytes = self.remove_silence(wav_bytes) # not required if works with silence microphone
        message = self.transcript_gateway.transcript_from_bytes(
            wav_bytes, raw_file_name.replace(".pcm", ".wav")
        )
        LOGGER.info("transcript end %s", message)
        return message

    def convert_from_raw_to_wav(self, audio_bytes: bytes):
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, "wb") as wav_file:
            wav_file.setnchannels(1)  # channels
            wav_file.setsampwidth(2)  # Set to 2 for 16-bit audio or 1 for 8-bit audio.
            wav_file.setframerate(32000)  #
            wav_file.writeframes(audio_bytes)
        wav_buffer.seek(0)
        wav_bytes = wav_buffer.read()
        return wav_bytes

    def convert_to_16000(self, audio_wav_bytes: bytes):
        audio_file = BytesIO(audio_wav_bytes)
        audio_input, sample_rate = sf.read(audio_file)
        # Resample the audio to 16,000 Hz
        audio_resampled = librosa.resample(
            audio_input, orig_sr=sample_rate, target_sr=16000
        )
        # Write the resampled audio back to bytes
        output_file = BytesIO()
        sf.write(output_file, audio_resampled, samplerate=16000, format="WAV")
        output_file.seek(0)  # Reset the pointer to the start of the BytesIO object
        return output_file.read()

    def remove_silence(
        self,
        audio_wav_bytes: bytes,
        silence_thresh: int = -40,
        min_silence_len: int = 1000,
    ) -> None:
        try:
            wav_buffer = io.BytesIO()
            audio = AudioSegment.from_file(io.BytesIO(audio_wav_bytes), format="wav")
            nonsilent_ranges = detect_nonsilent(
                audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh
            )
            # Combine non-silent segments
            processed_audio = AudioSegment.empty()
            for start, end in nonsilent_ranges:
                processed_audio += audio[start:end]

            # Export the processed audio to a BytesIO buffer
            wav_buffer = io.BytesIO()
            processed_audio.export(wav_buffer, format="wav")
            # Return the WAV bytes
            return wav_buffer.getvalue()
        except Exception as e:
            raise e
