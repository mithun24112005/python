# moves files of same type to their respective folders

import os


def createifnotexists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


# to create file is not in folder
files = os.listdir()
print(files)
createifnotexists("images")
createifnotexists("docs")
createifnotexists("media")

# to split ext and store in resspective lists
# os.path.splitext(file)[1].lower() --> file ext
imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
print(images)
docExts = [".txt", ".docx", ".doc", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
print(f"docs files are: {docs}")
mediaExts = [".mp4", ".mp3", ".flv"]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
print(f"media files are: {media}")
others = []

# to set other files in folder named others
# os.path.isfile(file) --> checks if it a file or not
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (
        (ext not in mediaExts)
        and (ext not in docExts)
        and (ext not in imgExts)
        and os.path.isfile(file)
    ):
        others.append(file)
print(f"other files are: {others}")

# to move corresponding file to respective folders
move("media", media)
move("images", images)
move("docs", docs)
move("others", others)
