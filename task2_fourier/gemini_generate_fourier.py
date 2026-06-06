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

Create a complete Manim scene demonstrating Fourier Series Decomposition of a square wave.
The scene should:
- Show the first 5 sine harmonics (n = 1, 3, 5, 7, 9)
- Draw each harmonic in a different color (BLUE, GREEN, RED, YELLOW, PURPLE)
- Show the cumulative sum updating step by step as each harmonic is added
- Include labeled axes (x and y)
- Include a title at the top of the screen
- Use wait() calls between each step so viewer can follow along

CRITICAL FONT RULES:
- You must NEVER use Tex() or MathTex()
- You must ONLY use the standard Text() class for all text
- Do NOT use get_graph() — use axes.plot() instead
- Do NOT use line_arg in axis config

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

# Save to fourier_series.py
with open("fourier_series.py", "w") as f:
    f.write(cleaned_code)

print("Done! Manim code saved to fourier_series.py")
