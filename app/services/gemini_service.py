print("========== GEMINI SERVICE LOADED ==========")
print(__file__)
from google import genai
import logging
import os

import os
from dotenv import load_dotenv
from google import genai

print("=== USING GEMINI SERVICE ===")

load_dotenv()

print("API Key Loaded:", os.getenv("GOOGLE_API_KEY"))

# Setup logging (important for debugging later)
logging.basicConfig(level=logging.INFO)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_event_with_gemini(event_name):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=event_name
        )

        # safe check (sometimes response.text can be None)
        if response and hasattr(response, "text"):
            return response.text

        return "No response from AI."

    except Exception as e:
        logging.error(f"Gemini API error: {e}")

        # fallback (app NEVER crashes)
        return "AI temporarily unavailable. Please try again later."
    