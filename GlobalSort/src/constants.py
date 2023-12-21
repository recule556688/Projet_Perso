
MENU_CHOICE = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
]  # List of the menu choices
EXTENSIONS_MUSIC = {  # Dictionary to store the extensions of the Music to be sorted
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".ogg": "Musique",
    ".wma": "Musique",
    ".m4a": "Musique",
    ".aac": "Musique",
    ".aiff": "Musique",
    ".ape": "Musique",
}
EXTENSIONS_VIDEO = {  # Dictionary to store the extensions of the Videos to be sorted
    ".mp4": "Videos",
    ".avi": "Videos",
    ".gif": "Videos",
    "avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".mov": "Videos",
}
EXTENSIONS_IMAGE = {  # Dictionary to store the extensions of the Images to be sorted
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".JPG": "Images",
    ".jpeg": "Images",
    ".heic": "Images",
    ".svg": "Images",
}
EXTENSIONS_DOCUMENT = (
    {  # Dictionary to store the extensions of the Documents to be sorted
        ".txt": "Documents",
        ".pptx": "Documents",
        ".csv": "Documents",
        ".xls": "Documents",
        ".odp": "Documents",
        ".pages": "Documents",
        ".pdf": "Documents",
        ".doc": "Documents",
        ".zip": "Documents",
        ".docx": "Documents",
    }
)
EXTENSIONS_DOWNLOAD = (
    {}
)  # Dictionary to store the extensions of the Download to be sorted
EXTENSIONS_DOWNLOAD.update(EXTENSIONS_DOCUMENT)
EXTENSIONS_DOWNLOAD.update(EXTENSIONS_IMAGE)
EXTENSIONS_DOWNLOAD.update(EXTENSIONS_VIDEO)
EXTENSIONS_DOWNLOAD.update(EXTENSIONS_MUSIC)
EXTENSIONS_DOWNLOAD.update(
    {
        ".exe": "executable",
        ".bat": "executable",
        ".sh": "executable",
        ".py": "executable",
        ".pyw": "executable",
        ".msi": "executable",
        ".apk": "executable",
        ".app": "executable",
        ".deb": "executable",
        ".rpm": "executable",
        ".bin": "executable",
        ".dmg": "executable",
        ".run": "executable",
        ".jar": "executable",
    }
)
