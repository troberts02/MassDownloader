## 🧩 Bulk File Downloader

Originally, this script was created to **download all the animated Pokémon sprites** from [Pokémon Showdown](https://play.pokemonshowdown.com/sprites/).
It automatically grabs all `.gif` sprite files from multiple subfolders and saves them neatly into folders on your computer.

However, it has since been updated to work as a **general-purpose mass downloader**, meaning you can use it to download **any file types** — images, icons, PDFs, ZIPs, or datasets — from **any open website directory**.

---

### 🖥️ Requirements

Before running the script, make sure you have Python installed along with the following libraries:

```bash
pip install requests beautifulsoup4
```

---

### 🚀 How to Run the Script

1. Save the script as `interactive_downloader.py`.

2. Open a terminal or command prompt in the folder where you saved it.

3. Run the script:

   ```bash
   python interactive_downloader.py
   ```

4. When prompted:

   * **Base URL:** The root of the site or directory you want to download from.
     Example:

     ```
     https://play.pokemonshowdown.com/sprites/
     ```
   * **Folders:** One or more subfolders separated by commas.
     Example:

     ```
     ani, ani-back, ani-shiny, ani-back-shiny
     ```
   * **File types:** What file extensions to download.
     Example:

     ```
     .gif
     ```
   * **Save folder:** Where to store everything.
     Press Enter to use the default (`Desktop\DownloadedFiles`) or enter your own path.

The program will automatically:

* Create the necessary folders.
* Download all matching files.
* Skip files that already exist.

---

### 🧩 Example — Pokémon Sprites (Original Purpose)

To recreate the original use case and download all animated Pokémon sprites:

```
Base URL: https://play.pokemonshowdown.com/sprites/
Folders: ani, ani-back, ani-shiny, ani-back-shiny
File types: .gif
Save folder: (press Enter for default)
```

Sprites will be downloaded into:

```
C:\Users\<YourName>\Desktop\DownloadedFiles\ani\
```

---

### 🌐 Using It for Non-Pokémon Websites

This script works with **any open directory-style website** — great for bulk downloading public files.

#### 🖼️ Example 1 — Download public image sets

```
Base URL: https://example.com/photos/
Folders: landscapes, portraits
File types: .jpg, .png
```

➡ Downloads all `.jpg` and `.png` images from both `/photos/landscapes/` and `/photos/portraits/`.

---

#### 📄 Example 2 — Download PDF documents

```
Base URL: https://researchhub.org/papers/
Folders: 2023, 2024
File types: .pdf
```

➡ Grabs all `.pdf` papers from the specified years.

---

#### 📦 Example 3 — Download datasets

```
Base URL: https://datasets.example.edu/public/
Folders: csv, zipfiles
File types: .csv, .zip
```

➡ Collects datasets and zipped archives from open data repositories.

---

### ⚙️ Tips for Customizing Downloads

* **Custom save location:**
  When asked for a save folder, type any valid path (e.g., `D:\MyDownloads\Images`).

* **Multiple file types:**
  Enter several at once, separated by commas (e.g. `.jpg, .png, .gif, .pdf`).

* **Single folder:**
  You can enter just one folder name (e.g. `icons`) if only one directory is needed.

* **Different websites:**
  As long as the website lists files directly (with visible file links), the script can download them.

---

### ⚠️ Notes & Best Practices

* Only use this on **websites that allow public access or downloading**.
  Do not use on login-protected or copyrighted sites.
* The script does **not** work with dynamically loaded content (like JavaScript galleries).
* Large sites may take time; re-running the script will skip already downloaded files.

---

### ✅ Example Output

```
📂 Checking https://example.com/photos/landscapes/ ...
  ⬇️ Downloading mountain.jpg...
  ⬇️ Downloading river.png...
✅ Finished landscapes -> C:\Users\David\Desktop\DownloadedFiles\landscapes

📂 Checking https://example.com/photos/portraits/ ...
  ⬇️ Downloading portrait1.jpg...
✅ Finished portraits -> C:\Users\David\Desktop\DownloadedFiles\portraits

🎉 All downloads complete!
```

---

## 🧠 Advanced Customization (For Developers)

You can easily modify the Python script to make it even more powerful.
Here are some ideas and how to implement them:

---

### 🔁 1. Recursive Subfolder Downloading

Currently, you specify folders manually (e.g., `ani`, `ani-shiny`).
To automatically download **all subfolders** listed on the main page:

**Modify this section:**

```python
folders_input = input("Enter folder names (comma-separated, e.g. ani, ani-back, ani-shiny): ")
folders = [f.strip().strip("/") + "/" for f in folders_input.split(",") if f.strip()]
```

**Replace it with:**

```python
# Automatically detect all subfolders if user leaves blank
resp = requests.get(root)
soup = BeautifulSoup(resp.text, "html.parser")
folders = [a.get("href") for a in soup.find_all("a") if a.get("href").endswith("/")]
print(f"Auto-detected folders: {folders}")
```

Now, pressing Enter without typing folders will make the script grab every listed subfolder.

---

### 🌍 2. Download Every File on a Page (No Folder Needed)

If you want to pull all files from a **single page** (e.g., all `.pdf`s on a research archive):

Skip folder inputs and modify this loop:

```python
for folder in folders:
    download_folder(folder)
```

Replace with:

```python
download_folder("")  # download directly from root URL
```

Then just set:

```
Base URL: https://example.com/files/
Folders: (leave blank)
File types: .pdf
```

---

### ⚡ 3. Change Which File Types Are Supported by Default

If you often download the same file types, you can set a default list:

```python
file_types = [".jpg", ".png", ".gif", ".pdf"]
```

Then skip typing them every time you run the script.

---

### 🧩 4. Add Retry or Timeout Handling

To make downloads more stable on slow connections:

```python
r = requests.get(file_url, timeout=10)
if r.status_code == 200:
    with open(file_path, "wb") as f:
        f.write(r.content)
else:
    print(f"⚠️ Skipped {href} (HTTP {r.status_code})")
```

---

### 📂 5. Automatically Name Folders After the Website

You can have it auto-name the save directory based on the base URL:

```python
from urllib.parse import urlparse
domain_name = urlparse(root).netloc.replace(".", "_")
base_save = os.path.join(os.path.expanduser("~"), "Desktop", domain_name)
```

This would create folders like:

```
Desktop\play_pokemonshowdown_com\
```

---

### 🎉 Summary

This downloader started as a simple Pokémon sprite collector but has evolved into a **flexible, general-purpose bulk downloader** for any type of public web directory.

Whether you’re grabbing:

* Sprites for game dev
* Stock photos for design
* PDFs for research
* or ZIP archives for data science

…this script can handle it — and can be easily customized for your specific needs.
