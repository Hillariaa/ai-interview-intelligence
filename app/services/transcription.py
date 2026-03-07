from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")


def transcribe_audio(audio_path: str):
    segments, _ = model.transcribe(audio_path)

    transcript = []

    for segment in segments:
        transcript.append(segment.text)

    return " ".join(transcript)
