import locale
from .menu import (
    generate_menu,
    display_help_fr,
    display_help_en,
    display_help_es,
    display_help_it,
    display_help_de,
    display_help_ru,
)


LANGUAGE_FUNCTIONS = {  # Define the dictionary
    "fr": {
        "menu": generate_menu("fr"),
        "help": display_help_fr,
        "color": "\033[1;31m",
        "invalid_choice_message": "Veuillez entrer un choix valide",
    },
    "en": {
        "menu": generate_menu("en"),
        "help": display_help_en,
        "color": "\033[1;32m",
        "invalid_choice_message": "Please enter a valid choice",
    },
    "es": {
        "menu": generate_menu("es"),
        "help": display_help_es,
        "color": "\033[1;33m",
        "invalid_choice_message": "Por favor ingrese una opción válida",
    },
    "it": {
        "menu": generate_menu("it"),
        "help": display_help_it,
        "color": "\033[1;34m",
        "invalid_choice_message": "Si prega di inserire una scelta valida",
    },
    "de": {
        "menu": generate_menu("de"),
        "help": display_help_de,
        "color": "\033[1;35m",
        "invalid_choice_message": "Bitte geben Sie eine gültige Auswahl ein",
    },
    "ru": {
        "menu": generate_menu("ru"),
        "help": display_help_ru,
        "color": "\033[1;36m",
        "invalid_choice_message": "Пожалуйста, введите действительный выбор",
    },
}
DIRECTORY_NAMES = {  # Map directory names to the correct language
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
LOG_MESSAGES = {  # Map log messages to the correct language
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

# Get the system language
lang = locale.getlocale()[0].split("_")[0]

# Get the correct log messages based on the OS language (default to English)

messages = LOG_MESSAGES.get(locale.getlocale()[0][:2], LOG_MESSAGES["en"])
# Get the correct directory names based on the OS language (default to English)

directories_name = DIRECTORY_NAMES.get(lang, DIRECTORY_NAMES["en"])
