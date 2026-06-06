# Manim GenAI Assignment

## Project Overview

This project uses the **Google Generative AI (Gemini) API** to automatically generate
Manim animation code for two mathematical concepts:

1. **Pythagorean Theorem** — A visual geometric proof showing a² + b² = c²
2. **Fourier Series Decomposition** — A square wave built from sine harmonics step by step

The generated Manim code is critically evaluated for quality, correctness, and visual clarity.

---

## Repository Structure

```
manim-genai-assignment/
├── README.md
├── requirements.txt
├── .gitignore
├── generate_scene.py
│
├── task1_pythagorean/
│   ├── gemini_generate_pythagoras.py
│   ├── pythagoras.py
│   └── output/
│       └── pythagoras_output.mp4
│
├── task2_fourier/
│   ├── gemini_generate_fourier.py
│   ├── fourier_series.py
│   └── output/
│       └── fourier_output.mp4
│
└── analysis/
    └── critical_analysis.md
```

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- FFmpeg installed and added to system PATH
- LaTeX (MiKTeX on Windows, MacTeX on macOS)
- A Google Gemini API key from https://aistudio.google.com/app/apikey

### Step 1 — Clone the Repository
```bash
git clone https://github.com/yash-iitk/manim-genai-assignment.git
cd manim-genai-assignment
```

### Step 2 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Set Up Your API Key
Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## How to Generate Manim Code Using Gemini

### Using the Interactive Generator
```bash
python generate_scene.py
```
Type your animation idea when prompted. The script will call Gemini and save the output as a `.py` file.

### Task 1 — Generate Pythagorean Theorem Code
```bash
cd task1_pythagorean
python gemini_generate_pythagoras.py
```

### Task 2 — Generate Fourier Series Code
```bash
cd task2_fourier
python gemini_generate_fourier.py
```

---

## How to Render Each Manim Scene

### Task 1 — Pythagorean Theorem
```bash
manim -pql task1_pythagorean/pythagoras.py PythagorasScene
```

### Task 2 — Fourier Series
```bash
manim -pql task2_fourier/fourier_series.py FourierSquareWave
```

**Quality flags:**
| Flag | Quality | Resolution |
|------|---------|------------|
| -pql | Low | 480p (fast, for testing) |
| -pqm | Medium | 720p |
| -pqh | High | 1080p (for final export) |

---

## Critical Analysis Findings

### Task 1 — Pythagorean Theorem
The Gemini-generated scene had the following key issues:
- Hardcoded triangle values that limit generalizability
- Squares not geometrically anchored to triangle sides
- Missing wait() calls making animation too fast to follow
- No color legend connecting colors to sides a, b, c
- Algebraic text overflowing outside the screen boundary

### Task 2 — Fourier Series
The Gemini-generated scene had the following key issues:
- No legend connecting harmonic colors to their term numbers
- Y-axis range mismatch causing wave clipping
- Cumulative sum not visually distinguished from individual harmonics
- No title or annotation explaining the mathematical concept
- Animation too fast for the viewer to follow the progression

Full detailed critique with fixes: see `analysis/critical_analysis.md`

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| Google Gemini API | AI code generation |
| Manim | Mathematical animation rendering |
| Python | Main programming language |
| python-dotenv | Secure API key management |
| Git & GitHub | Version control and submission |
