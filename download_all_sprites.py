import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base domain
root = "https://play.pokemonshowdown.com/sprites/"

# Subfolders you want to grab
folders = [
    "ani/",
    "ani-back/",
    "ani-shiny/",
    "ani-back-shiny/"
]

# Local save folder -> Desktop\PokemonSprites
base_save = os.path.join(os.path.expanduser("~"), "Desktop", "PokemonSprites")

# Function to download one folder
def download_folder(folder):
    url = urljoin(root, folder)
    save_path = os.path.join(base_save, folder.strip("/"))
    os.makedirs(save_path, exist_ok=True)

    print(f"📂 Checking {url} ...")
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    for a in soup.find_all("a"):
        href = a.get("href")
        if href and href.lower().endswith(".gif"):
            file_url = urljoin(url, href)
            file_path = os.path.join(save_path, href)

            if os.path.exists(file_path):
                print(f"  ⏩ Skipping {href} (already exists)")
                continue

            print(f"  ⬇️ Downloading {href}...")
            r = requests.get(file_url)
            with open(file_path, "wb") as f:
                f.write(r.content)

    print(f"✅ Finished {folder} -> {save_path}")

# Download each folder
for folder in folders:
    download_folder(folder)

print("\n🎉 All sprite folders downloaded successfully!")
