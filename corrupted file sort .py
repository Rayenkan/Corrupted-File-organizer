import os
import shutil


def lista(t, path):
    l = []
    for j in os.listdir(path):
        if t in j.lower():
            l.append(j)
    return l


while True:
    path = input("give the path: ")
    if os.path.exists(path):
        break
    else:
        print("Invalid path. Please provide a valid path.")

types = [".exe", ".jpg", ".png", ".pdf", ".mp4", ".rar", ".zip", ".docx", ".txt",
         ".gif", ".tif", ".jpeg", ".mov", ".avi", ".mp3", ".wav", ".html", ".css", ".js",
         ".py", ".java", ".php", ".xml", ".json", ".sql", ".dat",
         ".xlsx", ".xls", ".pptx", ".ppt", ".doc"]

for t in types:
    files = lista(t, path)

    if files:
        ch = os.path.join(path, "downloaded_" + t)

        if not os.path.exists(ch):
            os.mkdir(ch)

        for f in files:
            dow = os.path.join(path, f)
            new_path = os.path.join(ch, f)

            try:
                shutil.move(dow, new_path)
            except shutil.Error as e:
                print(f"Error moving file {f}: {e}")
