from fastapi import APIRouter, UploadFile, File
import os
from app.services.transcription import transcribe_audio
from app.services.interview_analysis import analyze_interview
from app.models.interview_models import InterviewResponse

router = APIRouter()


@router.post("/analyze-interview", response_model=InterviewResponse)
async def analyze(file: UploadFile = File(...)):

    audio_path = f"temp_{file.filename}"

    with open(audio_path, "wb") as f:
        f.write(await file.read())

    transcript = transcribe_audio(audio_path)

    os.remove(audio_path)

    analysis = analyze_interview(transcript)

    return {"transcript": transcript, "analysis": analysis}
