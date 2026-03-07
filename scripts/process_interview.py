from app.services.transcription import transcribe_audio
from app.services.interview_analysis import analyze_interview

audio_file = "data/hilary_interview.wav"

transcript = transcribe_audio(audio_file)

print("\nTranscript:\n")
print(transcript)

analysis = analyze_interview(transcript)

print("\nInterview Analysis:\n")
print(analysis)
