from dotenv import load_dotenv
import os
import json
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_interview(transcript: str):

    prompt = f"""
    You are an AI recruiter assistant.

    Analyze the following interview transcript.

    Schema:
    
    {{
    "skills": [],
    "technologies": [],
    "strengths": [],
    "weaknesses": [],
    "hire_recommendation": "Hire | Maybe | No Hire",
    "confidence_score": 0-100,
    "reasoning": ""
    }}

    Rules: 
    - confidence_score must be an integer between 0 and 100
    - Do NOT return decimals
    - Do NOT include explanations
    - Return only JSON

    Transcript:
    {transcript}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a technical hiring evaluator."},
            {"role": "user", "content": prompt},
        ],
    )

    analysis = response.choices[0].message.content

    if analysis is None:
        raise ValueError("LLM returned empty analysis")

    return json.loads(analysis)
