from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Topic(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "ViralMind AI Backend Running"}

@app.post("/generate-linkedin")
def generate_linkedin(data: Topic):

    prompt = f"""
    Write a professional LinkedIn post about {data.topic}.

    Include:
    - Strong Hook
    - Main Content
    - Call To Action
    - Relevant Hashtags
    """

    response = model.generate_content(prompt)

    return {
        "linkedin_post": response.text
    }


@app.post("/generate-instagram")
def generate_instagram(data: Topic):

    prompt = f"""
    Create a viral Instagram caption about {data.topic}

    Include:
    - Hook
    - Caption
    - Emojis
    - Hashtags
    """

    response = model.generate_content(prompt)

    return {"caption": response.text}


@app.post("/generate-reel")
def generate_reel(data: Topic):

    prompt = f"""
    Create a 30-second Instagram Reel script about {data.topic}

    Include:
    - Hook
    - Scene-by-scene script
    - CTA
    """

    response = model.generate_content(prompt)

    return {"reel_script": response.text}


@app.post("/viral-ideas")
def viral_ideas(data: Topic):

    prompt = f"""
    Generate 10 viral content ideas about {data.topic}
    """

    response = model.generate_content(prompt)

    return {"ideas": response.text}
