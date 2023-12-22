#!/usr/bin/python3
from src.constants import (
    MENU_CHOICE,
    EXTENSIONS_MUSIC,
    EXTENSIONS_VIDEO,
    EXTENSIONS_IMAGE,
    EXTENSIONS_DOCUMENT,
    EXTENSIONS_DOWNLOAD,
)
from src.logger import setup_logging
from src.menu import print_message
from src.language import os_language, directories_name, messages, LANGUAGE_FUNCTIONS
from src.utils import sort_files, clear_console
from src.undo import undo_all_operations
from pathlib import Path
import sys
from colorama import Fore, Style


def run():  # Main function that runs the program
    sorted_flag = False  # Flag to keep track if any file has been moved
    sorted_folders = set()  # Set to keep track of the sorted folders
    while True:
        language_functions = LANGUAGE_FUNCTIONS.get(
            os_language, LANGUAGE_FUNCTIONS["en"]
        )
        user_choice = input(language_functions["menu"])
        print(Fore.BLUE + "--" * 50 + Style.RESET_ALL)
        if user_choice not in MENU_CHOICE:
            clear_console()
            print_message(
                language_functions["color"],
                language_functions["invalid_choice_message"],
            )
            print(Fore.BLUE + "-" * 100 + Style.RESET_ALL)
            continue
        elif user_choice == "1":  # Sort music files
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Music"], EXTENSIONS_MUSIC, sorted_flag
            )
            clear_console()
            sorted_folders.update(new_folders)
        elif user_choice == "2":  # Sort video files
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Videos"], EXTENSIONS_VIDEO, sorted_flag
            )
            clear_console()
            sorted_folders.update(new_folders)
        elif user_choice == "3":  # Sort image files
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Images"], EXTENSIONS_IMAGE, sorted_flag
            )
            clear_console()
            sorted_folders.update(new_folders)
        elif user_choice == "4":  # Sort document files
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Documents"],
                EXTENSIONS_DOCUMENT,
                sorted_flag,
            )
            clear_console()
            sorted_folders.update(new_folders)
        elif user_choice == "5":  # Sort download files
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Downloads"],
                EXTENSIONS_DOWNLOAD,
                sorted_flag,
            )
            clear_console()
            sorted_folders.update(new_folders)
        elif user_choice == "6":  # Sort a specific folder
            try:
                print(Fore.BLUE + "{}".format("-" * 100) + Style.RESET_ALL)
                Custom_DIR = Path(
                    input(
                        Fore.BLUE + "{}".format(
                            "Enter the path of the folder? ".center(100, " ")
                        ) + Style.RESET_ALL
                    )
                )
                if not Custom_DIR.exists():
                    print(Fore.BLUE + "{}".format("-" * 100) + Style.RESET_ALL)
                    print(
                        Fore.RED + "{}".format(
                            "The specified path does not exist.".center(100, " ")
                        ) + Style.RESET_ALL
                    )
                    print(Fore.BLUE + "{}".format("-" * 100) + Style.RESET_ALL)
                    return
                sorted_flag, new_folders = sort_files(
                    Custom_DIR, EXTENSIONS_DOWNLOAD, sorted_flag
                )
                clear_console()
                sorted_folders.update(new_folders)
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
        elif user_choice == "7":  # Sort all the directories
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Music"], EXTENSIONS_MUSIC, sorted_flag
            )
            clear_console()
            sorted_folders.update(new_folders)
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Videos"], EXTENSIONS_VIDEO, sorted_flag
            )
            clear_console()
            sorted_folders.update(new_folders)
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Images"], EXTENSIONS_IMAGE, sorted_flag
            )
            clear_console()
            sorted_folders.update(new_folders)
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Downloads"],
                EXTENSIONS_DOWNLOAD,
                sorted_flag,
            )
            clear_console()
            sorted_folders.update(new_folders)
            sorted_flag, new_folders = sort_files(
                Path.home() / directories_name["Documents"],
                EXTENSIONS_DOCUMENT,
                sorted_flag,
            )
            clear_console()
            sorted_folders.update(new_folders)
            if sorted_flag:  # Only print if any file has been moved
                clear_console()
                for folder in sorted_folders:
                    print(
                        Fore.BLUE + "{}\n".format("-" * 100) + Fore.BLUE + "{}".format(
                            messages["file_sorted"]
                            .format(directory=folder)
                            .center(100),
                        ) + Style.RESET_ALL
                    )
            else:  # Print a different message if no files have been moved
                clear_console()
                print(
                    Fore.BLUE + "{}\n".format("-" * 100) + Fore.RED + "{}".format("No files were moved.".center(100)) + Style.RESET_ALL
                )
        elif user_choice == "8":  # Add a folder to the sorting program
            return
        elif user_choice == "9":  # Revert the changes
            clear_console()
            undo_all_operations()
        elif user_choice == "10":  # Quit the program
            print(Fore.BLUE + "-" * 100 + Style.RESET_ALL)
            if os_language == "fr":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.RED
                    + "Fermeture du programme".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "en":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.GREEN
                    + "Closing the program".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "es":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.YELLOW
                    + "Cerrando el programa".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "it":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.BLUE
                    + "Chiusura del programma".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "de":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.MAGENTA
                    + "Schließen des Programms".center(100)
                    + Style.RESET_ALL
                )
            elif os_language == "ru":
                clear_console()
                print(
                    Fore.BLUE
                    + "-" * 100
                    + "\n"
                    + Fore.CYAN
                    + "Закрытие программы".center(100)
                    + Style.RESET_ALL
                )
            print(Fore.BLUE + "-" * 100 + Style.RESET_ALL)
            sys.exit()
        elif user_choice == "11":  # Display the help menu
            clear_console()
            print(language_functions["help"])
            continue

def main():  # Main function
    setup_logging()
    run()

if __name__ == "__main__":  # Run the main function
    main()
