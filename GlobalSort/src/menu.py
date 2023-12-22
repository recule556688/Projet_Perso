from colorama import Fore, Style


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
        Fore.BLUE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
    ]

    menu = "\n".join(
        f"{colors[i%len(colors)]}{option.center(100)}{Style.RESET_ALL}"
        for i, option in enumerate(menu_options.get(language, menu_options["en"]))
    )
    return f"{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{menu}\n{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{Fore.GREEN}{'↪ Your Choice : '.center(100)}{Style.RESET_ALL}"


def generate_help_menu(
    language,
):  # Function to generate the help menu in the correct language
    help_options = {
        "fr": [
            "OPTIONS D'AIDE:",
            "1. Trier les fichiers musicaux: Cette option triera tous les fichiers musicaux.",
            "2. Trier les fichiers vidéo: Cette option triera tous les fichiers vidéo.",
            "3. Trier les fichiers image: Cette option triera tous les fichiers image.",
            "4. Trier les fichiers de document: Cette option triera tous les fichiers de document.",
            "5. Trier les fichiers de téléchargement: Cette option triera tous les fichiers de téléchargement.",
            "6. Trier les fichiers d'un répertoire spécifique: Cette option triera tous les fichiers d'un répertoire spécifique.",
            "7. Trier tous les répertoires: Cette option triera tous les fichiers de tous les répertoires inclue de base dans le programme.",
            "8. Ajouter un répertoire au programme de tri: Cette option ajoutera un nouveau répertoire au programme de tri.",
            "9. Annuler la dernière opération: Cette option annulera la dernière opération de tri effectuée.",
            "10. Quitter le programme: Cette option fermera le programme.",
            "11. Afficher le menu d'aide: Cette option affichera ce menu d'aide.",
        ],
        "en": [
            "HELP OPTIONS:",
            "1. Sort music files: This option will sort all music files.",
            "2. Sort video files: This option will sort all video files.",
            "3. Sort image files: This option will sort all image files.",
            "4. Sort document files: This option will sort all document files.",
            "5. Sort download files: This option will sort all download files.",
            "6. Sort files from a specific directory: This option will sort all files from a specific directory.",
            "7. Sort all directories: This option will sort all files from all directories.",
            "8. Add a directory to the sorting program: This option will add a new directory to the sorting program.",
            "9. Undo last operation: This option will undo the last sorting operation performed.",
            "10. Quit the program: This option will close the program.",
            "11. Display the help menu: This option will display this help menu.",
        ],
        "es": [
            "OPCIONES DE AYUDA:",
            "1. Ordenar archivos de música: Esta opción ordenará todos los archivos de música.",
            "2. Ordenar archivos de video: Esta opción ordenará todos los archivos de video.",
            "3. Ordenar archivos de imagen: Esta opción ordenará todos los archivos de imagen.",
            "4. Ordenar archivos de documento: Esta opción ordenará todos los archivos de documento.",
            "5. Ordenar archivos de descarga: Esta opción ordenará todos los archivos de descarga.",
            "6. Ordenar archivos de un directorio específico: Esta opción ordenará todos los archivos de un directorio específico.",
            "7. Ordenar todos los directorios: Esta opción ordenará todos los archivos de todos los directorios.",
            "8. Agregar un directorio al programa de clasificación: Esta opción agregará un nuevo directorio al programa de clasificación.",
            "9. Deshacer la última operación: Esta opción deshará la última operación de clasificación realizada.",
            "10. Salir del programa: Esta opción cerrará el programa.",
            "11. Mostrar el menú de ayuda: Esta opción mostrará este menú de ayuda.",
        ],
        "it": [
            "OPZIONI DI AIUTO:",
            "1. Ordina file musicali: Questa opzione ordinerà tutti i file musicali.",
            "2. Ordina file video: Questa opzione ordinerà tutti i file video.",
            "3. Ordina file di immagini: Questa opzione ordinerà tutti i file di immagini.",
            "4. Ordina file di documenti: Questa opzione ordinerà tutti i file di documenti.",
            "5. Ordina file di download: Questa opzione ordinerà tutti i file di download.",
            "6. Ordina file da una directory specifica: Questa opzione ordinerà tutti i file da una directory specifica.",
            "7. Ordina tutte le directory: Questa opzione ordinerà tutti i file da tutte le directory.",
            "8. Aggiungi una cartella al programma di ordinamento: Questa opzione aggiungerà una nuova cartella al programma di ordinamento.",
            "9. Annulla l'ultima operazione: Questa opzione annullerà l'ultima operazione di ordinamento eseguita.",
            "10. Esci dal programma: Questa opzione chiuderà il programma.",
            "11. Visualizza il menu di aiuto: Questa opzione visualizzerà questo menu di aiuto.",
        ],
        "de": [
            "HILFE OPTIONEN:",
            "1. Musikdateien sortieren: Diese Option sortiert alle Musikdateien.",
            "2. Videodateien sortieren: Diese Option sortiert alle Videodateien.",
            "3. Bilddateien sortieren: Diese Option sortiert alle Bilddateien.",
            "4. Dokumentdateien sortieren: Diese Option sortiert alle Dokumentdateien.",
            "5. Download-Dateien sortieren: Diese Option sortiert alle Download-Dateien.",
            "6. Dateien aus einem bestimmten Verzeichnis sortieren: Diese Option sortiert alle Dateien aus einem bestimmten Verzeichnis.",
            "7. Alle Verzeichnisse sortieren: Diese Option sortiert alle Dateien aus allen Verzeichnissen.",
            "8. Ordner zum Sortierprogramm hinzufügen: Diese Option fügt dem Sortierprogramm einen neuen Ordner hinzu.",
            "9. Letzte Operation rückgängig machen: Diese Option macht die letzte Sortieroperation rückgängig.",
            "10. Programm beenden: Diese Option schließt das Programm.",
            "11. Hilfe anzeigen: Diese Option zeigt dieses Hilfe-Menü an.",
        ],
        "ru": [
            "ПОМОЩЬ ОПЦИИ:",
            "1. Сортировать музыкальные файлы: Эта опция отсортирует все музыкальные файлы.",
            "2. Сортировать видео файлы: Эта опция отсортирует все видео файлы.",
            "3. Сортировать файлы изображений: Эта опция отсортирует все файлы изображений.",
            "4. Сортировать документы: Эта опция отсортирует все документы.",
            "5. Сортировать файлы для скачивания: Эта опция отсортирует все файлы для скачивания.",
            "6. Сортировать файлы из определенного каталога: Эта опция отсортирует все файлы из определенного каталога.",
            "7. Сортировать все каталоги: Эта опция отсортирует все файлы из всех каталогов.",
            "8. Добавить папку в программу сортировки: Эта опция добавит новую папку в программу сортировки.",
            "9. Отменить последнюю операцию: Эта опция отменит последнюю выполненную операцию сортировки.",
            "10. Выйти из программы: Эта опция закроет программу.",
            "11. Показать меню помощи: Эта опция отобразит это меню помощи.",
        ],
    }

    colors = [
        Fore.BLUE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
    ]

    help_menu = "\n".join(
        f"{colors[i%len(colors)]}{option.center(100)}{Style.RESET_ALL}"
        for i, option in enumerate(help_options.get(language, help_options["en"]))
    )
    return f"{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{help_menu}\n{Fore.BLUE}{'-'*100}{Style.RESET_ALL}\n{Fore.GREEN}{'↪ Your Choice : '.center(100)}{Style.RESET_ALL}"


def print_message(color, message):  # Function to print a message in the correct color
    print(f"{color}{message}{Style.RESET_ALL}")
