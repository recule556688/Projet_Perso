# Importing required standard library modules
from pathlib import (
    Path,
)  # For handling filesystem paths in a way that is compatible with all OS
import sys  # To interact with the Python interpreter
import locale  # To set the locale for your program
import logging  # To enable logging of events for debugging
import shutil  # To perform high-level file operations
import os  # To interact with the operating system

DIRECTORY_NAMES = { # Map directory names to the correct language
    "en": {
        "Music": "Music",
        "Videos": "Videos",
        "Images": "Images",
        "Documents": "Documents",
        "Downloads": "Downloads",
    },
    "fr": {
        "Music": "Musique",
        "Videos": "Vidéos",
        "Images": "Images",
        "Documents": "Documents",
        "Downloads": "Téléchargements",
    },
    "es": {
        "Music": "Música",
        "Videos": "Videos",
        "Images": "Imágenes",
        "Documents": "Documentos",
        "Downloads": "Descargas",
    },
    "it": {
        "Music": "Musica",
        "Videos": "Video",
        "Images": "Immagini",
        "Documents": "Documenti",
        "Downloads": "Scaricati",
    },
    "de": {
        "Music": "Musik",
        "Videos": "Videos",
        "Images": "Bilder",
        "Documents": "Dokumente",
        "Downloads": "Downloads",
    },
    "ru": {
        "Music": "Музыка",
        "Videos": "Видео",
        "Images": "Изображения",
        "Documents": "Документы",
        "Downloads": "Загрузки",
    },
}


LOG_MESSAGES = { # Map log messages to the correct language
    "en": {
        "dir_not_exist": "The directory {directory} does not exist.",
        "error_moving": "Error moving file {file}: {error}",
        "file_sorted": "The file {directory} has been sorted",
        "moved": "Moved file from {src} to {dst}",
        "no_operation_to_cancel": "There is no operation to cancel.",
    },
    "fr": {
        "dir_not_exist": "Le répertoire {directory} n'existe pas.",
        "error_moving": "Erreur lors du déplacement du fichier {file}: {error}",
        "file_sorted": "Le fichier {directory} a bien été trié",
        "moved": "Fichier déplacé de {src} à {dst}",
        "no_operation_to_cancel": "Il n'y a aucune opération à annuler.",
    },
    "es": {
        "dir_not_exist": "El directorio {directory} no existe.",
        "error_moving": "Error al mover el archivo {file}: {error}",
        "file_sorted": "El archivo {directory} ha sido ordenado",
        "moved": "Archivo movido de {src} a {dst}",
        "no_operation_to_cancel": "No hay operación para cancelar.",
    },
    "it": {
        "dir_not_exist": "La directory {directory} non esiste.",
        "error_moving": "Errore durante lo spostamento del file {file}: {error}",
        "file_sorted": "Il file {directory} è stato ordinato",
        "moved": "File spostato da {src} a {dst}",
        "no_operation_to_cancel": "Non c'è alcuna operazione da annullare.",
    },
    "de": {
        "dir_not_exist": "Das Verzeichnis {directory} existiert nicht.",
        "error_moving": "Fehler beim Verschieben der Datei {file}: {error}",
        "file_sorted": "Die Datei {directory} wurde sortiert",
        "moved": "Datei von {src} nach {dst} verschoben",
        "no_operation_to_cancel": "Es gibt keine Operation zum Abbrechen.",
    },
    "ru": {
        "dir_not_exist": "Каталог {directory} не существует.",
        "error_moving": "Ошибка при перемещении файла {file}: {error}",
        "file_sorted": "Файл {directory} был отсортирован",
        "moved": "Файл перемещен из {src} в {dst}",
        "no_operation_to_cancel": "Нет операции для отмены.",
    },
}

# Get the user's operating system language
os_language = locale.getlocale()[0][:2] if locale.getlocale()[0] else "en"


logging.basicConfig( # Configure the logging module
    filename="file_sorter.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

# Get the system language
lang = locale.getlocale()[0].split("_")[0]

# Get the correct directory names based on the OS language (default to English)
directories_name = DIRECTORY_NAMES.get(lang, DIRECTORY_NAMES["en"])

# Create an empty stack to store undo operations
undo_stack = []

# Get the correct log messages based on the OS language (default to English)
messages = LOG_MESSAGES.get(locale.getlocale()[0][:2], LOG_MESSAGES["en"])

MENU_CHOICE = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] # List of the menu choices

EXTENSIONS_MUSIC = { # Dictionary to store the extensions of the Music to be sorted
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
EXTENSIONS_VIDEO = { # Dictionary to store the extensions of the Videos to be sorted
    ".mp4": "Videos",
    ".avi": "Videos",
    ".gif": "Videos",
    "avi": "Videos",
    ".mkv": "Videos",
    ".wmv": "Videos",
    ".mov": "Videos",
}
EXTENSIONS_IMAGE = { # Dictionary to store the extensions of the Images to be sorted
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".JPG": "Images",
    ".jpeg": "Images",
    ".heic": "Images",
    ".svg": "Images",
}
EXTENSIONS_DOCUMENT = { # Dictionary to store the extensions of the Documents to be sorted
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
EXTENSIONS_DOWNLOAD = {} # Dictionary to store the extensions of the Download to be sorted
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


def generate_menu(language): # Function to generate the menu in the correct language
    menu_options = {
        "fr": [
            "OPTIONS DE MENU:",
            "1. Trier les fichiers de musique",
            "2. Trier les fichiers de vidéo",
            "3. Trier les fichiers de images",
            "4. Trier les fichiers de documents",
            "5. Trier les fichiers de download",
            "6. Trier les fichiers d'un dossier spécifique",
            "7. Trier tous les répertoires",
            "8. Annuler la dernière opération",
            "9. Quitter le programme",
            "10. Afficher le menu d'aide",
        ],
        "en": [
            "MENU OPTIONS:",
            "1. Sort music files",
            "2. Sort video files",
            "3. Sort image files",
            "4. Sort document files",
            "5. Sort download files",
            "6. Sort files from a specific directory",
            "7. Sort all directories",
            "8. Undo last operation",
            "9. Quit the program",
            "10. Display help menu",
        ],
        "es": [
            "OPCIONES DE MENÚ:",
            "1. Ordenar archivos de música",
            "2. Ordenar archivos de video",
            "3. Ordenar archivos de imágenes",
            "4. Ordenar archivos de documentos",
            "5. Ordenar archivos de descarga",
            "6. Ordenar archivos de un directorio específico",
            "7. Ordenar todos los directorios",
            "8. Deshacer la última operación",
            "9. Salir del programa",
            "10. Mostrar el menú de ayuda",
        ],
        "it": [
            "OPZIONI MENU:",
            "1. Ordina i file musicali",
            "2. Ordina i file video",
            "3. Ordina i file immagine",
            "4. Ordina i file di documento",
            "5. Ordina i file di download",
            "6. Ordina i file da una directory specifica",
            "7. Ordina tutte le directory",
            "8. Annulla l'ultima operazione",
            "9. Esci dal programma",
            "10. Visualizza il menu di aiuto",
        ],
        "de": [
            "MENÜOPTIONEN:",
            "1. Musikdateien sortieren",
            "2. Videodateien sortieren",
            "3. Bilddateien sortieren",
            "4. Dokumentdateien sortieren",
            "5. Download-Dateien sortieren",
            "6. Dateien aus einem bestimmten Verzeichnis sortieren",
            "7. Alle Verzeichnisse sortieren",
            "8. Letzte Operation rückgängig machen",
            "9. Programm beenden",
            "10. Hilfe-Menü anzeigen",
        ],
        "ru": [
            "ОПЦИИ МЕНЮ:",
            "1. Сортировать музыкальные файлы",
            "2. Сортировать видео файлы",
            "3. Сортировать файлы изображений",
            "4. Сортировать документы",
            "5. Сортировать файлы для скачивания",
            "6. Сортировать файлы из определенного каталога",
            "7. Сортировать все каталоги",
            "8. Отменить последнюю операцию",
            "9. Выйти из программы",
            "10. Показать меню помощи",
        ],
    }

    colors = [
        "\033[1;34m",
        "\033[1;31m",
        "\033[1;32m",
        "\033[1;33m",
        "\033[1;34m",
        "\033[1;35m",
        "\033[1;36m",
        "\033[1;37m",
        "\033[1;31m",
        "\033[1;32m",
        "\033[1;33m",
    ]

    menu = "\n".join(
        f"{colors[i%len(colors)]}{option.center(100)}\033[0m"
        for i, option in enumerate(menu_options.get(language, menu_options["en"]))
    )
    return f"\033[1;34m{'-'*100}\033[0m\n{menu}\n\033[1;34m{'-'*100}\033[0m\n{'↪ Your Choice : '.center(100)}"


def display_help_fr():  # function to display the help menu in French
    print(
        "\033[1;34m{}\n\033[1;34m{}\n\033[1;34m{}\033[0m"
        "\n\033[1;31m{}\033[0m"
        "\n\033[1;32m{}\033[0m"
        "\n\033[1;33m{}\033[0m"
        "\n\033[1;34m{}\033[0m"
        "\n\033[1;35m{}\033[0m"
        "\n\033[1;36m{}\033[0m"
        "\n\033[1;37m{}\033[0m"
        "\n\033[1;31m{}\033[0m"
        "\n\033[1;32m{}\033[0m"
        "\n\033[1;33m{}\033[0m\n".format(
            "-" * 100,
            "OPTIONS DE MENU:".center(100),
            "-" * 100,
            "1. Trier les fichiers musicaux: Cette option triera tous les fichiers musicaux.".center(
                100
            ),
            "2. Trier les fichiers vidéo: Cette option triera tous les fichiers vidéo.".center(
                100
            ),
            "3. Trier les fichiers image: Cette option triera tous les fichiers image.".center(
                100
            ),
            "4. Trier les fichiers de document: Cette option triera tous les fichiers de document.".center(
                100
            ),
            "5. Trier les fichiers de téléchargement: Cette option triera tous les fichiers de téléchargement.".center(
                100
            ),
            "6. Trier les fichiers d'un répertoire spécifique: Cette option triera tous les fichiers d'un répertoire spécifique.".center(
                100
            ),
            "7. Trier tous les répertoires: Cette option triera tous les fichiers de tous les répertoires.".center(
                100
            ),
            "8. Annuler la dernière opération: Cette option annulera la dernière opération de tri effectuée.".center(
                100
            ),
            "9. Quitter le programme: Cette option fermera le programme.".center(100),
            "10. Aide: Affiche ce message d'aide.".center(100),
        )
    )


def display_help_en():  # Function to display the help menu in English
    print(
        f"\033[1;34m{'-'*100}"
        f"\n\033[1;34m{'MENU OPTIONS:'.center(100)}"
        f"\n\033[1;34m{'-'*100}\033[0m"
        f"\n\033[1;31m{'1. Sort music files: This option will sort all music files.'.center(100)}\033[0m"
        f"\n\033[1;32m{'2. Sort video files: This option will sort all video files.'.center(100)}\033[0m"
        f"\n\033[1;33m{'3. Sort image files: This option will sort all image files.'.center(100)}\033[0m"
        f"\n\033[1;34m{'4. Sort document files: This option will sort all document files.'.center(100)}\033[0m"
        f"\n\033[1;35m{'5. Sort download files: This option will sort all download files.'.center(100)}\033[0m"
        f"\n\033[1;36m{'6. Sort files from a specific directory: This option will sort all files from a specific directory.'.center(100)}\033[0m"
        f"\n\033[1;37m{'7. Sort all directories: This option will sort all files from all directories.'.center(100)}\033[0m"
        f"\n\033[1;31m{'8. Undo last operation: This option will undo the last sorting operation performed.'.center(100)}\033[0m"
        f"\n\033[1;32m{'9. Quit the program: This option will close the program.'.center(100)}\033[0m"
        f"\n\033[1;33m{'10. Help: Displays this help message.'.center(100)}\033[0m\n"
    )


def display_help_es():  # Function to display the help menu in Spanish
    print(
        f"\033[1;34m{'-'*100}"
        f"\n\033[1;34m{'OPCIONES DE MENÚ:'.center(100)}"
        f"\n\033[1;34m{'-'*100}\033[0m"
        f"\n\033[1;31m{'1. Ordenar archivos de música: Esta opción ordenará todos los archivos de música.'.center(100)}\033[0m"
        f"\n\033[1;32m{'2. Ordenar archivos de video: Esta opción ordenará todos los archivos de video.'.center(100)}\033[0m"
        f"\n\033[1;33m{'3. Ordenar archivos de imagen: Esta opción ordenará todos los archivos de imagen.'.center(100)}\033[0m"
        f"\n\033[1;34m{'4. Ordenar archivos de documento: Esta opción ordenará todos los archivos de documento.'.center(100)}\033[0m"
        f"\n\033[1;35m{'5. Ordenar archivos de descarga: Esta opción ordenará todos los archivos de descarga.'.center(100)}\033[0m"
        f"\n\033[1;36m{'6. Ordenar archivos de un directorio específico: Esta opción ordenará todos los archivos de un directorio específico.'.center(100)}\033[0m"
        f"\n\033[1;37m{'7. Ordenar todos los directorios: Esta opción ordenará todos los archivos de todos los directorios.'.center(100)}\033[0m"
        f"\n\033[1;31m{'8. Deshacer la última operación: Esta opción deshará la última operación de ordenamiento realizada.'.center(100)}\033[0m"
        f"\n\033[1;32m{'9. Salir del programa: Esta opción cerrará el programa.'.center(100)}\033[0m"
        f"\n\033[1;33m{'10. Ayuda: Muestra este mensaje de ayuda.'.center(100)}\033[0m\n"
    )


def display_help_it():  # Function to display the help menu in Italian
    print(
        "\033[1;34m{}\n\033[1;34m{}\n\033[1;34m{}\033[0m"
        "\n\033[1;31m{}\033[0m"
        "\n\033[1;32m{}\033[0m"
        "\n\033[1;33m{}\033[0m"
        "\n\033[1;34m{}\033[0m"
        "\n\033[1;35m{}\033[0m"
        "\n\033[1;36m{}\033[0m"
        "\n\033[1;37m{}\033[0m"
        "\n\033[1;31m{}\033[0m"
        "\n\033[1;32m{}\033[0m"
        "\n\033[1;33m{}\033[0m\n".format(
            "-" * 100,
            "OPZIONI DI MENU:".center(100),
            "-" * 100,
            "1. Ordina file musicali: Questa opzione ordinerà tutti i file musicali.".center(
                100
            ),
            "2. Ordina file video: Questa opzione ordinerà tutti i file video.".center(
                100
            ),
            "3. Ordina file di immagini: Questa opzione ordinerà tutti i file di immagini.".center(
                100
            ),
            "4. Ordina file di documenti: Questa opzione ordinerà tutti i file di documenti.".center(
                100
            ),
            "5. Ordina file di download: Questa opzione ordinerà tutti i file di download.".center(
                100
            ),
            "6. Ordina file da una directory specifica: Questa opzione ordinerà tutti i file da una directory specifica.".center(
                100
            ),
            "7. Ordina tutte le directory: Questa opzione ordinerà tutti i file da tutte le directory.".center(
                100
            ),
            "8. Annulla l'ultima operazione: Questa opzione annullerà l'ultima operazione di ordinamento eseguita.".center(
                100
            ),
            "9. Esci dal programma: Questa opzione chiuderà il programma.".center(100),
            "10. Aiuto: Mostra questo messaggio di aiuto.".center(100),
        )
    )


def display_help_de():  # Function to display the help menu in German
    print(
        f"\033[1;34m{'-'*100}"
        f"\n\033[1;34m{'MENÜOPTIONEN:'.center(100)}"
        f"\n\033[1;34m{'-'*100}\033[0m"
        f"\n\033[1;31m{'1. Musikdateien sortieren: Diese Option sortiert alle Musikdateien.'.center(100)}\033[0m"
        f"\n\033[1;32m{'2. Videodateien sortieren: Diese Option sortiert alle Videodateien.'.center(100)}\033[0m"
        f"\n\033[1;33m{'3. Bilddateien sortieren: Diese Option sortiert alle Bilddateien.'.center(100)}\033[0m"
        f"\n\033[1;34m{'4. Dokumentdateien sortieren: Diese Option sortiert alle Dokumentdateien.'.center(100)}\033[0m"
        f"\n\033[1;35m{'5. Download-Dateien sortieren: Diese Option sortiert alle Download-Dateien.'.center(100)}\033[0m"
        f"\n\033[1;36m{'6. Dateien aus einem bestimmten Verzeichnis sortieren: Diese Option sortiert alle Dateien aus einem bestimmten Verzeichnis.'.center(100)}\033[0m"
        f"\n\033[1;37m{'7. Alle Verzeichnisse sortieren: Diese Option sortiert alle Dateien aus allen Verzeichnissen.'.center(100)}\033[0m"
        f"\n\033[1;31m{'8. Letzte Operation rückgängig machen: Diese Option macht die letzte Sortieroperation rückgängig.'.center(100)}\033[0m"
        f"\n\033[1;32m{'9. Programm beenden: Diese Option schließt das Programm.'.center(100)}\033[0m"
        f"\n\033[1;33m{'10. Hilfe: Zeigt diese Hilfemeldung an.'.center(100)}\033[0m\n"
    )


def display_help_ru():  # Function to display the help menu in Russian
    print(
        f"\033[1;34m{'-'*100}"
        f"\n\033[1;34m{'ОПЦИИ МЕНЮ:'.center(100)}"
        f"\n\033[1;34m{'-'*100}\033[0m"
        f"\n\033[1;31m{'1. Сортировать музыкальные файлы: Эта опция отсортирует все музыкальные файлы.'.center(100)}\033[0m"
        f"\n\033[1;32m{'2. Сортировать видеофайлы: Эта опция отсортирует все видеофайлы.'.center(100)}\033[0m"
        f"\n\033[1;33m{'3. Сортировать файлы изображений: Эта опция отсортирует все файлы изображений.'.center(100)}\033[0m"
        f"\n\033[1;34m{'4. Сортировать документы: Эта опция отсортирует все документы.'.center(100)}\033[0m"
        f"\n\033[1;35m{'5. Сортировать файлы для скачивания: Эта опция отсортирует все файлы для скачивания.'.center(100)}\033[0m"
        f"\n\033[1;36m{'6. Сортировать файлы из определенного каталога: Эта опция отсортирует все файлы из определенного каталога.'.center(100)}\033[0m"
        f"\n\033[1;37m{'7. Сортировать все каталоги: Эта опция отсортирует все файлы из всех каталогов.'.center(100)}\033[0m"
        f"\n\033[1;31m{'8. Отменить последнюю операцию: Эта опция отменит последнюю операцию сортировки.'.center(100)}\033[0m"
        f"\n\033[1;32m{'9. Выйти из программы: Эта опция закроет программу.'.center(100)}\033[0m"
        f"\n\033[1;33m{'10. Показать меню помощи: Это покажет это сообщение с помощью.'.center(100)}\033[0m\n"
    )


def sort_files(directory, extensions): # Function to sort files
    if not directory.exists():
        print(
            "\033[1;34m{}\n\033[1;31m{}\033[0m".format(
                "-" * 100,
                messages["dir_not_exist"].format(directory=directory).center(100),
            )
        )
        return

    files = [f for f in directory.iterdir() if f.is_file()]
    for file in files:
        dossier_cible = extensions.get(file.suffix.lower(), "Divers")
        dossier_cible_absolu = directory / dossier_cible
        dossier_cible_absolu.mkdir(exist_ok=True)
        fichier_cible = dossier_cible_absolu / file.name
        try:
            file.rename(fichier_cible)
            undo_stack.append((fichier_cible, file))
            logging.info(
                "\033[1;34m{}\n\033[1;32m{}\033[0m".format(
                    "-" * 100,
                    messages["moved"].format(src=file, dst=fichier_cible).center(100),
                )
            )
        except Exception as e:
            print(
                "\033[1;34m{}\n\033[1;31m{}\033[0m".format(
                    "-" * 100,
                    messages["error_moving"]
                    .format(file=file.name, error=e)
                    .center(100),
                )
            )
            logging.error(
                "\033[1;34m{}\n\033[1;31m{}\033[0m".format(
                    "-" * 100,
                    messages["error_moving"].format(file=file, error=e).center(100),
                )
            )

    clear_console()
    print(
        "\033[1;34m{}\n\033[1;34m{}\033[0m".format(
            "-" * 100, messages["file_sorted"].format(directory=directory).center(100)
        )
    )


def undo_all_operations(): # Function to undo all operations
    while undo_stack:
        undo_last_operation()


def undo_last_operation(): # Function to undo the last operation
    global undo_stack  # Use the global undo_stack
    global messages  # Use the global messages

    if undo_stack:
        src, dst = undo_stack.pop()
        shutil.move(src, dst)
        logging.info(messages["moved"].format(src=src, dst=dst))
    else:
        print(messages["no_operation_to_cancel"])
        return


def clear_console(): # Function to clear the console
    os.system("cls" if os.name == "nt" else "clear")


def main(): # Main function
    while True:
        if os_language == "fr":
            user_choice = input(generate_menu("fr"))
        elif os_language == "en":
            user_choice = input(generate_menu("en"))
        elif os_language == "es":
            user_choice = input(generate_menu("es"))
        elif os_language == "it":
            user_choice = input(generate_menu("it"))
        elif os_language == "de":
            user_choice = input(generate_menu("de"))
        elif os_language == "ru":
            user_choice = input(generate_menu("ru"))
        else:
            user_choice = input(
                MENU_en
            )  # default to English if language is not recognized
            print("--" * 50)
        if user_choice not in MENU_CHOICE:
            if os_language == "fr":
                clear_console()
                print(
                    "\033[1;34m{}\n\033[1;31m{}\033[0m".format(
                        "-" * 100, "Veuillez entrer un choix valide".center(100)
                    )
                )
            elif os_language == "en":
                clear_console()
                print(
                    "\033[1;34m{}\n\033[1;32m{}\033[0m".format(
                        "-" * 100, "Please enter a valid choice".center(100)
                    )
                )
            elif os_language == "es":
                clear_console()
                print(
                    "\033[1;34m{}\n\033[1;33m{}\033[0m".format(
                        "-" * 100, "Por favor ingrese una opción válida".center(100)
                    )
                )
            elif os_language == "it":
                clear_console()
                print(
                    "\033[1;34m{}\n\033[1;34m{}\033[0m".format(
                        "-" * 100, "Si prega di inserire una scelta valida".center(100)
                    )
                )
            elif os_language == "de":
                clear_console()
                print(
                    "\033[1;34m{}\n\033[1;35m{}\033[0m".format(
                        "-" * 100,
                        "Bitte geben Sie eine gültige Auswahl ein".center(100),
                    )
                )
            elif os_language == "ru":
                clear_console()
                print(
                    "\033[1;34m{}\n\033[1;36m{}\033[0m".format(
                        "-" * 100,
                        "Пожалуйста, введите действительный выбор".center(100),
                    )
                )
            print("\033[1;34m" + "-" * 100 + "\033[0m")
            continue
        if user_choice == "1":  # Sort music files
            sort_files(Path.home() / directories_name["Music"], EXTENSIONS_MUSIC)
        elif user_choice == "2":  # Sort video files
            sort_files(Path.home() / directories_name["Videos"], EXTENSIONS_VIDEO)
        elif user_choice == "3":  # Sort image files
            sort_files(Path.home() / directories_name["Images"], EXTENSIONS_IMAGE)
        elif user_choice == "4":  # Sort document files
            sort_files(Path.home() / directories_name["Documents"], EXTENSIONS_DOCUMENT)
        elif user_choice == "5":  # Sort download files
            sort_files(Path.home() / directories_name["Downloads"], EXTENSIONS_DOWNLOAD)
        elif user_choice == "6":  # Sort a specific folder
            Custom_DIR = Path(input("Entrer le chemin du dossier ? "))
            sort_files(Custom_DIR, EXTENSIONS_DOWNLOAD)
        elif user_choice == "7":  # Sort all the directories
            sort_files(Path.home() / directories_name["Music"], EXTENSIONS_MUSIC)
            sort_files(Path.home() / directories_name["Videos"], EXTENSIONS_VIDEO)
            sort_files(Path.home() / directories_name["Images"], EXTENSIONS_IMAGE)
            sort_files(Path.home() / directories_name["Documents"], EXTENSIONS_DOCUMENT)
            sort_files(Path.home() / directories_name["Downloads"], EXTENSIONS_DOWNLOAD)
        elif user_choice == "8":  # Revert the changes
            clear_console()
            undo_all_operations()
        elif user_choice == "9":  # Quit the program
            print("\033[1;34m" + "-" * 100)
            if os_language == "fr":
                clear_console()
                print(
                    "\033[1;34m"
                    + "-" * 100
                    + "\n\033[1;31m"
                    + "Fermeture du programme".center(100)
                )
            elif os_language == "en":
                clear_console()
                print(
                    "\033[1;34m"
                    + "-" * 100
                    + "\n\033[1;32m"
                    + "Closing the program".center(100)
                )
            elif os_language == "es":
                clear_console()
                print(
                    "\033[1;34m"
                    + "-" * 100
                    + "\n\033[1;33m"
                    + "Cerrando el programa".center(100)
                )
            elif os_language == "it":
                clear_console()
                print(
                    "\033[1;34m"
                    + "-" * 100
                    + "\n\033[1;34m"
                    + "Chiusura del programma".center(100)
                )
            elif os_language == "de":
                clear_console()
                print(
                    "\033[1;34m"
                    + "-" * 100
                    + "\n\033[1;35m"
                    + "Schließen des Programms".center(100)
                )
            elif os_language == "ru":
                clear_console()
                print(
                    "\033[1;34m"
                    + "-" * 100
                    + "\n\033[1;36m"
                    + "Закрытие программы".center(100)
                )
            print("\033[1;34m" + "-" * 100 + "\033[0m")
            sys.exit()
        elif user_choice == "10":  # Display the help menu
            if os_language == "fr":
                clear_console()
                display_help_fr()
            elif os_language == "en":
                clear_console()
                display_help_en()
            elif os_language == "es":
                clear_console()
                display_help_es()
            elif os_language == "it":
                clear_console()
                display_help_it()
            elif os_language == "de":
                clear_console()
                display_help_de()
            elif os_language == "ru":
                clear_console()
                display_help_ru()
            continue


if __name__ == "__main__": # Run the main function
    main()
