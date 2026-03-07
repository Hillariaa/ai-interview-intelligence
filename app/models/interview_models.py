from pydantic import BaseModel
from typing import List


class InterviewAnalysis(BaseModel):
    skills: List[str]
    technologies: List[str]
    strengths: List[str]
    weaknesses: List[str]
    hire_recommendation: str
    confidence_score: int
    reasoning: str


class InterviewResponse(BaseModel):
    transcript: str
    analysis: InterviewAnalysis
