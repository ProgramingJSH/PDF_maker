# src/pdf_maker/config.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INPUT_FILE = BASE_DIR / "input/lyrics.txt"
TEMPLATE_FILE = BASE_DIR / "templates/study_template_ink_save.html"
OUTPUT = BASE_DIR / "output"
