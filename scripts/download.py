# 💀 Deprecated, Use Git LFS instead for sample images
from pathlib import Path
import gdown

DATA_DIR = Path(".") / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

# FOLDER_ID = "1F8FJlA5aNMh5oig67NJRbnA0NGTu19IO"
# FOLDER_URL = f"https://drive.google.com/drive/folders/{FOLDER_ID}"
ID = "1F8FJlA5aNMh5oig67NJRbnA0NGTu19IO"


def download():
    print("Make directories")
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading...")
    # gdown.download_folder(url=FOLDER_URL, output=str(INPUT_DIR), quiet=False)
    gdown.download_folder(
        id=ID,
        output=str(INPUT_DIR),
        quiet=False,
    )
    print("Download completed!!!")


if __name__ == "__main__":
    download()
