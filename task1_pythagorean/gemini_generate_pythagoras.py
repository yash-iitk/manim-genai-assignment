import os
import re
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

# Prompt sent to Gemini
prompt = """
You are an expert in Python and the Manim animation library.
Generate ONLY valid Python code using Manim for the following:

Create a complete Manim scene that visually proves the Pythagorean Theorem (a2 + b2 = c2).
The scene should:
- Draw a right triangle with sides labeled a, b, and c
- Build three squares on each side of the triangle
- Shade each square in a different color (BLUE for a, GREEN for b, RED for c)
- Display the algebraic identity a2 + b2 = c2 as text on screen
- Use proper animation steps with wait() calls between each step

CRITICAL FONT RULES:
- You must NEVER use Tex() or MathTex()
- You must ONLY use the standard Text() class for all text

Do not include any explanations or additional text.
Just output the raw Python code.
"""

print("Sending prompt to Gemini, please wait...")
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt
)

# Clean the response (remove markdown fences if present)
def extract_python_code(raw_text):
    backticks = chr(96) * 3
    pattern = rf"{backticks}(?:python)?\n(.*?)\n{backticks}"
    match = re.search(pattern, raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_text.strip()

cleaned_code = extract_python_code(response.text)

# Save to pythagoras.py
with open("pythagoras.py", "w") as f:
    f.write(cleaned_code)

print("Done! Manim code saved to pythagoras.py")
