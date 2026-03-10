# AI Interview Intelligence API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Whisper](https://img.shields.io/badge/Speech%20to%20Text-Whisper-purple)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI-black)
![Docker](https://img.shields.io/badge/Docker-Container-blue)

Interact with the system here: 

https://ai-interview-intelligence.onrender.com/docs

also use my very own audio bio and get to know me:

[data_hilary_interview.wav](https://github.com/user-attachments/files/25859419/data_hilary_interview.wav)


---

AI Interview Intelligence is an applied AI system that analyzes interview responses from audio recordings.  
It combines **speech recognition and large language models** to transcribe candidate answers and generate structured interview insights for recruiters.

The system demonstrates how modern AI pipelines can connect **speech models, LLM reasoning, and production APIs** to build practical AI-powered hiring tools.

---

# Features

- Audio interview transcription using **Whisper**
- Automated interview analysis using **OpenAI LLMs**
- Extracts:
  - Candidate skills
  - Technologies mentioned
  - Strengths
  - Weaknesses
  - Hiring recommendation
  - Confidence score
- Production-ready **FastAPI backend**
- Structured responses using **Pydantic models**
- **Docker containerization**
- **CI/CD with GitHub Actions**

---

# Architecture

Audio Interview
↓
Whisper Transcription
↓
Transcript Processing
↓
LLM Interview Analysis
↓
Structured JSON Output
↓
FastAPI API Response

---

# Tech Stack

**AI / ML**

- OpenAI API
- Whisper (faster-whisper)

**Backend**

- Python
- FastAPI
- Pydantic

**Infrastructure**

- Docker
- GitHub Actions (CI/CD)

---

# Tech Stack

**AI / ML**

- OpenAI API
- Whisper (faster-whisper)

**Backend**

- Python
- FastAPI
- Pydantic

**Infrastructure**

- Docker
- GitHub Actions (CI/CD)

---

# API Endpoint

## Analyze Interview

**POST**
/analyze-interview

Use my mini audio bio:

[data_hilary_interview.wav](https://github.com/user-attachments/files/25859382/data_hilary_interview.wav)

---

Upload an interview audio file.

Example response:
```
json

{

  "transcript": "...",

  "analysis": {

    "skills": [],

    "technologies": [],

    "strengths": [],

    "weaknesses": [],

    "hire_recommendation": "Hire",

    "confidence_score": 92

  }

}
```
---

# Local Development

Install dependencies:

```
uv sync
```

Run the API:

```
uv run uvicorn app.main:app --reload
```

Open docs:

```
http://localhost:8000/docs
```

---

# Docker

Build the container:

```
docker build -t ai-interview-intelligence .
```

Run the container:

```
docker run -p 8000:8000 --env-file .env ai-interview-intelligence
```

---

# Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key
```

---

# Example Use Case

This system could be used to:

- Automatically summarize candidate interviews
- Assist recruiters with structured evaluations
- Identify key skills mentioned in candidate responses
- Provide AI-assisted hiring recommendations

---

# Project Purpose

This project demonstrates **applied AI engineering**, specifically how to integrate:

- Speech AI
- LLM reasoning
- Structured outputs
- Production APIs
- Containerized deployment

The focus is on building **real AI systems rather than isolated models**.

---

# Author

Hilary Azimoh — Applied AI Engineer
