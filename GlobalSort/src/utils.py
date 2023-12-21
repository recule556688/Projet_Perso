import os
from .undo import undo_stack
from .language import messages
from .logger import log_message


def sort_files(directory, extensions, sorted_flag):  # Add sorted as an argument
    sorted_folders = set()  # Set to keep track of the sorted folders
    if not directory.exists():
        return (
            sorted_flag,
            sorted_folders,
        )  # Return sorted and sorted_folders if the directory does not exist

    files = [f for f in directory.iterdir() if f.is_file()]
    for file in files:
        dossier_cible = extensions.get(file.suffix.lower(), "Divers")
        dossier_cible_absolu = directory / dossier_cible
        fichier_cible = dossier_cible_absolu / file.name
        if (
            file.parent != dossier_cible_absolu
        ):  # Check if the file is not in the correct folder
            try:
                file.rename(fichier_cible)
                undo_stack.append((fichier_cible, file))
                sorted_flag = True  # Set the flag to True if a file has been moved
                sorted_folders.add(
                    str(dossier_cible_absolu)
                )  # Add the folder to the sorted folders set
                print(
                    f"\033[1;32m{'Successfully moved ' + str(file) + ' to ' + str(dossier_cible_absolu).center(100)}\033[0m"
                )  # Print a success message in green
                log_message(
                    "info", messages["moved"].format(src=file, dst=dossier_cible_absolu)
                )
            except Exception as e:
                print(
                    f"Exception when moving file: {e}"
                )  # Print the exception if one is thrown
                log_message("error", messages["exception"].format(exception=e))

    return sorted_flag, sorted_folders  # Return the sorted flag and the sorted folders


def clear_console():  # Function to clear the console
    os.system("cls" if os.name == "nt" else "clear")
    log_message("info", messages["console_cleared"])
