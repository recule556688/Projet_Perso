from pathlib import Path
import sys

MENU_CHOICE = ["1", "2", "3", "4", "5", "6", "7"]

MENU = """
1. Trier les fichiers de musique
2. Trier les fichiers de vidéo
3. Trier les fichiers de images
4. Trier les fichiers de documents
5. Trier les fichiers de download
6. Trier les fichiers de d'un autre dossier spécifique
7. Quitter le programme
↪ Votre Choix : """


EXTENSIONS_MUSIC = {
    ".mp3": "Musique",
    ".wav": "Musique",
}
EXTENSIONS_VIDEO = {
    ".mp4": "Videos",
    ".avi": "Videos",
    ".gif": "Videos",
}
EXTENSIONS_IMAGE = {
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".JPG": "Images",
}
EXTENSIONS_DOCUMENT = {
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
EXTENSIONS_ALL = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".JPG": "Images",
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
    ".iso": "Fichier_ISO",
    ".iso.torrent": "Fichier_ISO",
    ".torrent": "Fichier_ISO",
    ".jar": "Jar",
    ".html": "Html",
    ".exe": "executable"
}

while True:
    print("--" * 50)
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICE:
        print("Veuillez choisir une option valide")
        continue

    if user_choice == "1":  # Trier les fichiers de musique
        Music_DIR = Path.home() / "Music"
        files = [f for f in Music_DIR.iterdir() if f.is_file()]
        for file in files:
            dossier_cible = EXTENSIONS_MUSIC.get(file.suffix, "Divers")
            dossier_cible_absolu = Music_DIR / dossier_cible
            dossier_cible_absolu.mkdir(exist_ok=True)
            fichier_cible = dossier_cible_absolu / file.name
            file.rename(fichier_cible)
        print(f"Le fichier {Music_DIR} a bien été trié")
    elif user_choice == "2":  # Trier les fichiers de vidéo
        Video_DIR = Path.home() / "Videos"
        files = [f for f in Video_DIR.iterdir() if f.is_file()]
        for file in files:
            dossier_cible = EXTENSIONS_VIDEO.get(file.suffix, "Divers")
            dossier_cible_absolu = Video_DIR / dossier_cible
            dossier_cible_absolu.mkdir(exist_ok=True)
            fichier_cible = dossier_cible_absolu / file.name
            file.rename(fichier_cible)
        print(f"Le fichier {Video_DIR} a bien été trié")
    elif user_choice == "3":  # Trier les fichiers de images
        Image_DIR = Path.home() / "Videos"
        files = [f for f in Image_DIR.iterdir() if f.is_file()]
        for file in files:
            dossier_cible = EXTENSIONS_IMAGE.get(file.suffix, "Divers")
            dossier_cible_absolu = Image_DIR / dossier_cible
            dossier_cible_absolu.mkdir(exist_ok=True)
            fichier_cible = dossier_cible_absolu / file.name
            file.rename(fichier_cible)
        print(f"Le fichier {Image_DIR} a bien été trié")
    elif user_choice == "4":  # Trier les fichiers de documents
        Document_DIR = Path.home() / "Videos"
        files = [f for f in Document_DIR.iterdir() if f.is_file()]
        for file in files:
            dossier_cible = EXTENSIONS_DOCUMENT.get(file.suffix, "Divers")
            dossier_cible_absolu = Document_DIR / dossier_cible
            dossier_cible_absolu.mkdir(exist_ok=True)
            fichier_cible = dossier_cible_absolu / file.name
            file.rename(fichier_cible)
        print(f"Le fichier {Document_DIR} a bien été trié")
    elif user_choice == "5":  # Trier les fichiers de download
        Download_DIR = Path.home() / "Downloads"
        files = [f for f in Download_DIR.iterdir() if f.is_file()]
        for file in files:
            dossier_cible = EXTENSIONS_ALL.get(file.suffix, "Divers")
            dossier_cible_absolu = Download_DIR / dossier_cible
            dossier_cible_absolu.mkdir(exist_ok=True)
            fichier_cible = dossier_cible_absolu / file.name
            file.rename(fichier_cible)
        print(f"Le fichier {Download_DIR} a bien été trié")
    elif user_choice == "6":  # Trier les fichiers d'un autre dossier spécifique
        Custom_DIR = Path(input("Entrer le chemin du dossier ? "))
        files = [f for f in Custom_DIR.iterdir() if f.is_file()]
        for file in files:
            dossier_cible = EXTENSIONS_ALL.get(file.suffix, "Divers")
            dossier_cible_absolu = Custom_DIR / dossier_cible
            dossier_cible_absolu.mkdir(exist_ok=True)
            fichier_cible = dossier_cible_absolu / file.name
            file.rename(fichier_cible)
        print(f"Le fichier {Custom_DIR} a bien été trié")
    elif user_choice == "7":  # Quitter le programme
        print("Fermeture du programme")
        print("--" * 50)
        sys.exit()
