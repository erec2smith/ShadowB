import os
import shutil

def florg(folder=None):
    if folder is None:
        return "The folder path is required!"
    types = {
        ".jpg": "Images", ".png": "Images", ".jpeg": "Images",
        ".zip": "Archives", ".rar": "Archives",
        ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
        ".mp3": "Music", ".wav": "Music",
        ".py": "Code", ".js": "Code", ".html": "Code",
        ".exe": "Code", ".cpp": "Code", ".css": "Code"
    }


    skip_folders = set(types.values())

    for root, dirs, files in os.walk(folder):

        dirs[:] = [d for d in dirs if d not in skip_folders]

        moved = 0
        for file in files:
            path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            if ext in types:
                target_folder = os.path.join(root, types[ext])
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(path, os.path.join(target_folder, file))
                print(f"{file} → {root}/{types[ext]}/")
                moved += 1
            else:
                print(f"Unknown extension: {file}")

        if moved > 0:
            print(f"\n Your files have been organized successfully: {root}\n")

