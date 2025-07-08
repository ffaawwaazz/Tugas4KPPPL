import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-pro")
response = model.generate_content("Apa hobi favoritmu dan mengapa kamu menyukainya?")
print(response.text)
