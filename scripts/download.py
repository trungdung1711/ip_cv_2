from pathlib import Path
import gdown

DATA_DIR = Path(".") / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

MAIN_URL = "https://drive.google.com/drive/folders/"
FOLDER_ID = "1F8FJlA5aNMh5oig67NJRbnA0NGTu19IO"

FOLDER_URL = MAIN_URL + FOLDER_ID


def download():
    # Making directories
    print("Make directories")
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading...")
    gdown.download_folder(
        url=FOLDER_URL, output=str(INPUT_DIR), use_cookies=False, quiet=False
    )
    print("Download completed!!!")


if __name__ == "__main__":
    download()
