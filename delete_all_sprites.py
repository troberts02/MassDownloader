import os
import shutil

# Base local folder where sprites were saved
base_save = os.path.join(os.path.expanduser("~"), "Desktop", "PokemonSprites")

# Subfolders you want to delete
folders = [
    "ani",
    "ani-back",
    "ani-shiny",
    "ani-back-shiny"
]

# Function to delete one folder
def delete_folder(folder):
    folder_path = os.path.join(base_save, folder)
    if os.path.exists(folder_path):
        print(f"🗑️ Deleting {folder_path} ...")
        shutil.rmtree(folder_path)
        print(f"✅ Deleted {folder_path}")
    else:
        print(f"⚠️ Folder {folder_path} does not exist, skipping.")

# Delete each folder
for folder in folders:
    delete_folder(folder)

# Optional: Delete the base folder if empty
if os.path.exists(base_save) and not os.listdir(base_save):
    print(f"🗑️ Deleting empty base folder {base_save} ...")
    os.rmdir(base_save)
    print(f"✅ Base folder deleted")

print("\n🎉 All sprite folders removed successfully!")
