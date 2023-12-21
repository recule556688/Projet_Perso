def generate_menu(language):  # Function to generate the menu in the correct language
    menu_options = {
        "fr": [
            "OPTIONS DE MENU:",
            "1 - Trier les fichiers de musique",
            "2 - Trier les fichiers de vidéo",
            "3 - Trier les fichiers de images",
            "4 - Trier les fichiers de documents",
            "5 - Trier les fichiers de download",
            "6 - Trier les fichiers d'un dossier spécifique",
            "7 - Trier tous les répertoires",
            "8 - Ajouter un dossier au programme de trie",
            "9 - Annuler la dernière opération",
            "10 - Quitter le programme",
            "11 - Afficher le menu d'aide",
        ],
        "en": [
            "MENU OPTIONS:",
            "1 - Sort music files",
            "2 - Sort video files",
            "3 - Sort image files",
            "4 - Sort document files",
            "5 - Sort download files",
            "6 - Sort files from a specific directory",
            "7 - Sort all directories",
            "8 - Add a folder to the sorting program",
            "9 - Undo last operation",
            "10 - Quit the program",
            "11 - Display the help menu",
        ],
        "es": [
            "OPCIONES DE MENÚ:",
            "1 - Ordenar archivos de música",
            "2 - Ordenar archivos de video",
            "3 - Ordenar archivos de imágenes",
            "4 - Ordenar archivos de documentos",
            "5 - Ordenar archivos de descarga",
            "6 - Ordenar archivos de un directorio específico",
            "7 - Ordenar todos los directorios",
            "8 - Agregar una carpeta al programa de clasificación",
            "9 - Deshacer la última operación",
            "10 - Salir del programa",
            "11 - Mostrar el menú de ayuda",
        ],
        "it": [
            "OPZIONI MENU:",
            "1 - Ordina i file musicali",
            "2 - Ordina i file video",
            "3 - Ordina i file immagine",
            "4 - Ordina i file di documento",
            "5 - Ordina i file di download",
            "6 - Ordina i file da una directory specifica",
            "7 - Ordina tutte le directory",
            "8 - Aggiungi una cartella al programma di ordinamento",
            "9 - Annulla l'ultima operazione",
            "10 - Esci dal programma",
            "11 - Visualizza il menu di aiuto",
        ],
        "de": [
            "MENÜOPTIONEN:",
            "1 - Musikdateien sortieren",
            "2 - Videodateien sortieren",
            "3 - Bilddateien sortieren",
            "4 - Dokumentdateien sortieren",
            "5 - Download-Dateien sortieren",
            "6 - Dateien aus einem bestimmten Verzeichnis sortieren",
            "7 - Alle Verzeichnisse sortieren",
            "8 - Ordner zum Sortierprogramm hinzufügen",
            "9 - Letzte Operation rückgängig machen",
            "10 - Programm beenden",
            "11 - Hilfe anzeigen",
        ],
        "ru": [
            "ОПЦИИ МЕНЮ:",
            "1 - Сортировать музыкальные файлы",
            "2 - Сортировать видео файлы",
            "3 - Сортировать файлы изображений",
            "4 - Сортировать документы",
            "5 - Сортировать файлы для скачивания",
            "6 - Сортировать файлы из определенного каталога",
            "7 - Сортировать все каталоги",
            "8 - Добавить папку в программу сортировки",
            "9 - Отменить последнюю операцию",
            "10 - Выйти из программы",
            "11 - Показать меню помощи",
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
    return f"\033[1;34m{'-'*100}\033[0m\n{menu}\n\033[1;34m{'-'*100}\033[0m\n\033[1;32m{'↪ Your Choice : '.center(100)}\033[0m"


def display_help_fr():  # function to display the help menu in French
    print(
        "\033[1;34m"
        + ("-" * 100)
        + "\n"
        + "\033[1;34m"
        + "OPTIONS DE MENU:".center(100)
        + "\n"
        + "\033[1;34m"
        + ("-" * 100)
        + "\033[0m"
        "\n\033[1;31m"
        + "1. Trier les fichiers musicaux: Cette option triera tous les fichiers musicaux.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "2. Trier les fichiers vidéo: Cette option triera tous les fichiers vidéo.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "3. Trier les fichiers image: Cette option triera tous les fichiers image.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;34m"
        + "4. Trier les fichiers de document: Cette option triera tous les fichiers de document.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;35m"
        + "5. Trier les fichiers de téléchargement: Cette option triera tous les fichiers de téléchargement.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;36m"
        + "6. Trier les fichiers d'un répertoire spécifique: Cette option triera tous les fichiers d'un répertoire spécifique.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;37m"
        + "7. Trier tous les répertoires: Cette option triera tous les fichiers de tous les répertoires.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;31m"
        + "8. Ajouter un répertoire au programme de tri: Cette option ajoutera un nouveau répertoire au programme de tri.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "9. Annuler la dernière opération: Cette option annulera la dernière opération de tri effectuée.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "10. Quitter le programme: Cette option fermera le programme.".center(100)
        + "\033[0m"
        "\n\033[1;34m"
        + "11. Aide: Affiche ce message d'aide.".center(100)
        + "\033[0m\n"
    )


def display_help_en():  # Function to display the help menu in English
    print(
        "\033[1;34m"
        + ("-" * 100)
        + "\n"
        + "\033[1;34m"
        + "MENU OPTIONS:".center(100)
        + "\n"
        + "\033[1;34m"
        + ("-" * 100)
        + "\033[0m"
        "\n\033[1;31m"
        + "1. Sort music files: This option will sort all music files.".center(100)
        + "\033[0m"
        "\n\033[1;32m"
        + "2. Sort video files: This option will sort all video files.".center(100)
        + "\033[0m"
        "\n\033[1;33m"
        + "3. Sort image files: This option will sort all image files.".center(100)
        + "\033[0m"
        "\n\033[1;34m"
        + "4. Sort document files: This option will sort all document files.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;35m"
        + "5. Sort download files: This option will sort all download files.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;36m"
        + "6. Sort files from a specific directory: This option will sort all files from a specific directory.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;37m"
        + "7. Sort all directories: This option will sort all files from all directories.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;31m"
        + "8. Add a directory to the sorting program: This option will add a new directory to the sorting program.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "9. Undo last operation: This option will undo the last sorting operation performed.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "10. Quit the program: This option will close the program.".center(100)
        + "\033[0m"
        "\n\033[1;34m"
        + "11. Help: Displays this help message.".center(100)
        + "\033[0m\n"
    )


def display_help_es():  # Function to display the help menu in Spanish
    print(
        "\033[1;34m"
        + ("-" * 100)
        + "\n"
        + "\033[1;34m"
        + "OPCIONES DE MENÚ:".center(100)
        + "\n"
        + "\033[1;34m"
        + ("-" * 100)
        + "\033[0m"
        "\n\033[1;31m"
        + "1. Ordenar archivos de música: Esta opción ordenará todos los archivos de música.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "2. Ordenar archivos de video: Esta opción ordenará todos los archivos de video.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "3. Ordenar archivos de imagen: Esta opción ordenará todos los archivos de imagen.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;34m"
        + "4. Ordenar archivos de documento: Esta opción ordenará todos los archivos de documento.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;35m"
        + "5. Ordenar archivos de descarga: Esta opción ordenará todos los archivos de descarga.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;36m"
        + "6. Ordenar archivos de un directorio específico: Esta opción ordenará todos los archivos de un directorio específico.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;37m"
        + "7. Ordenar todos los directorios: Esta opción ordenará todos los archivos de todos los directorios.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;31m"
        + "8. Agregar un directorio al programa de clasificación: Esta opción agregará un nuevo directorio al programa de clasificación.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "9. Deshacer la última operación: Esta opción deshará la última operación de clasificación realizada.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "10. Salir del programa: Esta opción cerrará el programa.".center(100)
        + "\033[0m"
        "\n\033[1;34m"
        + "11. Ayuda: Muestra este mensaje de ayuda.".center(100)
        + "\033[0m\n"
    )


def display_help_it():  # Function to display the help menu in Italian
    print(
        "\033[1;34m"
        + ("-" * 100)
        + "\n"
        + "\033[1;34m"
        + "OPZIONI DI MENU:".center(100)
        + "\n"
        + "\033[1;34m"
        + ("-" * 100)
        + "\033[0m"
        "\n\033[1;31m"
        + "1. Ordina file musicali: Questa opzione ordinerà tutti i file musicali.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "2. Ordina file video: Questa opzione ordinerà tutti i file video.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "3. Ordina file di immagini: Questa opzione ordinerà tutti i file di immagini.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;34m"
        + "4. Ordina file di documenti: Questa opzione ordinerà tutti i file di documenti.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;35m"
        + "5. Ordina file di download: Questa opzione ordinerà tutti i file di download.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;36m"
        + "6. Ordina file da una directory specifica: Questa opzione ordinerà tutti i file da una directory specifica.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;37m"
        + "7. Ordina tutte le directory: Questa opzione ordinerà tutti i file da tutte le directory.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;31m"
        + "8. Aggiungi una cartella al programma di ordinamento: Questa opzione aggiungerà una nuova cartella al programma di ordinamento.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "9. Annulla l'ultima operazione: Questa opzione annullerà l'ultima operazione di ordinamento eseguita.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "10. Esci dal programma: Questa opzione chiuderà il programma.".center(100)
        + "\033[0m"
        "\n\033[1;34m"
        + "11. Aiuto: Visualizza questo messaggio di aiuto.".center(100)
        + "\033[0m\n"
    )


def display_help_de():  # Function to display the help menu in German
    print(
        "\033[1;34m"
        + ("-" * 100)
        + "\n"
        + "\033[1;34m"
        + "MENÜOPTIONEN:".center(100)
        + "\n"
        + "\033[1;34m"
        + ("-" * 100)
        + "\033[0m"
        "\n\033[1;31m"
        + "1. Musikdateien sortieren: Diese Option sortiert alle Musikdateien.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "2. Videodateien sortieren: Diese Option sortiert alle Videodateien.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "3. Bilddateien sortieren: Diese Option sortiert alle Bilddateien.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;34m"
        + "4. Dokumentdateien sortieren: Diese Option sortiert alle Dokumentdateien.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;35m"
        + "5. Download-Dateien sortieren: Diese Option sortiert alle Download-Dateien.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;36m"
        + "6. Dateien aus einem bestimmten Verzeichnis sortieren: Diese Option sortiert alle Dateien aus einem bestimmten Verzeichnis.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;37m"
        + "7. Alle Verzeichnisse sortieren: Diese Option sortiert alle Dateien aus allen Verzeichnissen.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;31m"
        + "8. Ordner zum Sortierprogramm hinzufügen: Diese Option fügt dem Sortierprogramm einen neuen Ordner hinzu.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "9. Letzte Operation rückgängig machen: Diese Option macht die letzte Sortieroperation rückgängig.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "10. Programm beenden: Diese Option schließt das Programm.".center(100)
        + "\033[0m"
        "\n\033[1;34m"
        + "11. Hilfe anzeigen: Diese Option zeigt diese Hilfe an.".center(100)
        + "\033[0m\n"
    )


def display_help_ru():  # Function to display the help menu in Russian
    print(
        "\033[1;34m"
        + ("-" * 100)
        + "\n"
        + "\033[1;34m"
        + "ОПЦИИ МЕНЮ:".center(100)
        + "\n"
        + "\033[1;34m"
        + ("-" * 100)
        + "\033[0m"
        "\n\033[1;31m"
        + "1. Сортировать музыкальные файлы: Эта опция отсортирует все музыкальные файлы.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "2. Сортировать видеофайлы: Эта опция отсортирует все видеофайлы.".center(100)
        + "\033[0m"
        "\n\033[1;33m"
        + "3. Сортировать файлы изображений: Эта опция отсортирует все файлы изображений.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;34m"
        + "4. Сортировать документы: Эта опция отсортирует все документы.".center(100)
        + "\033[0m"
        "\n\033[1;35m"
        + "5. Сортировать файлы для скачивания: Эта опция отсортирует все файлы для скачивания.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;36m"
        + "6. Сортировать файлы из определенного каталога: Эта опция отсортирует все файлы из определенного каталога.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;37m"
        + "7. Сортировать все каталоги: Эта опция отсортирует все файлы из всех каталогов.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;31m"
        + "8. Добавить папку в программу сортировки: Эта опция добавит новую папку в программу сортировки.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;32m"
        + "9. Отменить последнюю операцию: Эта опция отменит последнюю выполненную операцию сортировки.".center(
            100
        )
        + "\033[0m"
        "\n\033[1;33m"
        + "10. Выйти из программы: Эта опция закроет программу.".center(100)
        + "\033[0m"
        "\n\033[1;34m"
        + "11. Показать меню помощи: Эта опция отобразит это сообщение справки.".center(
            100
        )
        + "\033[0m\n"
    )


def print_message(color, message): # Function to print a message in the correct color
    print(f"{color}{message}\033[0m")
