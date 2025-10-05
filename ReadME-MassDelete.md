## 🗑️ File & Folder Deletion Script

Originally, this script was created to **delete all previously downloaded Pokémon Showdown sprite folders** from your desktop.
It provided a quick way to clean up sprite collections like `ani/`, `ani-back/`, and `ani-shiny` after using the downloader script.

However, this version can also be used as a **universal file cleanup tool** — perfect for deleting files and folders from any type of project, website download, or dataset.

---

### 🖥️ Requirements

This script uses only Python’s built-in libraries — no external installations needed.

Works on **Windows, macOS, and Linux.**

---

### 🚀 How to Run

1. Save the file as `delete_all_sprites.py` (or rename it to something more general like `delete_files.py`).
2. Open a terminal or command prompt in the same folder as the script.
3. Run:

   ```bash
   python delete_all_sprites.py
   ```

The script will:

* Locate your Desktop folder.
* Find and delete the target folders.
* Optionally remove the parent folder if it becomes empty.

---

### 🧩 Default Behavior (Pokémon Sprites)

By default, the script deletes these folders:

```
Desktop\PokemonSprites\ani\
Desktop\PokemonSprites\ani-back\
Desktop\PokemonSprites\ani-shiny\
Desktop\PokemonSprites\ani-back-shiny\
```

When complete, it removes the base folder if it’s empty.

---

### 🌐 Using It for Non-Pokémon Folders or Websites

This same script can be used to clean up any files or folders downloaded from **other websites or projects**.

#### 🗂️ Example 1 — Remove Downloaded Image Sets

If you previously mass-downloaded images from another site and stored them in `Desktop\\DownloadedFiles`, modify:

```python
base_save = os.path.join(os.path.expanduser("~"), "Desktop", "PokemonSprites")
```

To:

```python
base_save = os.path.join(os.path.expanduser("~"), "Desktop", "DownloadedFiles")
```

Then update the folders list:

```python
folders = ["icons", "photos", "banners"]
```

This deletes your chosen image folders instead of Pokémon sprites.

---

#### 🧾 Example 2 — Clean Up Research PDFs or Datasets

If you used the downloader to grab files from a research archive or dataset site, set:

```python
base_save = os.path.join(os.path.expanduser("~"), "Downloads", "DataSets")
folders = ["pdfs", "csv", "results"]
```

This will delete all project data inside the `Downloads\\DataSets` folder.

---

#### 📁 Example 3 — Delete Everything Inside a Directory

To remove **everything inside a base folder** regardless of subfolder names, replace:

```python
for folder in folders:
    delete_folder(folder)
```

With:

```python
for folder in os.listdir(base_save):
    folder_path = os.path.join(base_save, folder)
    if os.path.isdir(folder_path):
        delete_folder(folder)
```

This version automatically deletes every folder under `base_save`.

---

### ⚙️ Optional: Delete Specific File Types

To delete certain file types (like `.gif`, `.jpg`, `.zip`) but keep folder structure, add this inside the `delete_folder()` function:

```python
for root, _, files in os.walk(folder_path):
    for file in files:
        if file.lower().endswith((".gif", ".png", ".zip")):
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"🗑️ Deleted file: {file_path}")
```

---

### ✅ Example Output

```
🗑️ Deleting C:\Users\David\Desktop\PokemonSprites\ani ...
✅ Deleted C:\Users\David\Desktop\PokemonSprites\ani
🗑️ Deleting C:\Users\David\Desktop\PokemonSprites\ani-shiny ...
✅ Deleted C:\Users\David\Desktop\PokemonSprites\ani-shiny
🎉 All folders removed successfully!
```

---

### ⚠️ Warnings

* ⚠️ **This script permanently deletes files.** Double-check all paths before running.
* To test safely, comment out the `shutil.rmtree(folder_path)` line and print the paths first.
* Do **not** use this to delete system folders or configuration files.

---

### 🧠 Summary

This script began as a simple cleanup tool for Pokémon sprite folders but can now handle **any bulk folder or file deletion task** — ideal for cleaning up large download directories or resetting projects.

You can use it to:

* Remove public image datasets
* Clean up bulk downloads from other websites
* Delete research files or archives after processing
* Quickly reset your local testing environment

It’s a flexible, safe, and customizable deletion utility that complements the bulk downloader perfectly.
