from pathlib import Path
import shutil

DATA_DIR = Path(".") / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

shutil.rmtree(INPUT_DIR)

INPUT_DIR.mkdir(parents=True, exist_ok=True)
