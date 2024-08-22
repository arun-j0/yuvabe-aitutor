# config.py
from dotenv import load_dotenv
import os

load_dotenv('sample.env')

youtube_api_key = os.getenv("YOUTUBE_API_KEY2")
groq_api_key = os.getenv("GROQ_API_KEY")
