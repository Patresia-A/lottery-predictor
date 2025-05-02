
import os
import requests
from datetime import datetime

# URLs for the New York Open Data lottery datasets
POWERBALL_URL = "https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD"
MEGAMILLIONS_URL = "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD"

# File paths to save downloaded CSVs
DATA_DIR = "data"
POWERBALL_CSV = os.path.join(DATA_DIR, "powerball.csv")
MEGAMILLIONS_CSV = os.path.join(DATA_DIR, "megamillions.csv")

def download_csv(url, output_path):
    print(f"Downloading data from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Saved to {output_path}")
    else:
        print(f"Failed to download from {url}, status code: {response.status_code}")

def fetch_lottery_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    print("Fetching Powerball and Mega Millions data...")
    download_csv(POWERBALL_URL, POWERBALL_CSV)
    download_csv(MEGAMILLIONS_URL, MEGAMILLIONS_CSV)
    print("Fetch complete:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    fetch_lottery_data()
