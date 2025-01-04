import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

model= genai.GenerativeModel(model_name='gemini-pro')

def generate_tech_questions(tech_stack):
    prompt = f"you are a assistant which generates total 5 technical interview questions based on tech stack: {tech_stack}'."
    response = model.generate_content(prompt)
    return response.text