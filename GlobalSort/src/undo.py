# Create an empty stack to store undo operations
import os
import shutil
from .logger import log_message
from .language import messages


undo_stack = []


def undo_all_operations():  # Function to undo all operations
    if not undo_stack:
        print("\033[1;34m{}\033[0m".format("-" * 100))
        print(
            "\033[1;33m{}\033[0m".format("There is no operation to cancel.".center(100))
        )
        log_message("info", messages["no_operation_to_cancel"])
        return
    while undo_stack:
        undo_last_operation()


def undo_last_operation():  # Function to undo the last operation
    if undo_stack:
        src, dst = undo_stack.pop()
        if os.path.exists(src):  # Check if the source file exists
            shutil.move(src, dst)
            print(
                f"\033[1;32m{'Successfully moved ' + str(src) + ' back to ' + str(dst).center(100)}\033[0m"
            )  # Print a success message in green
            log_message("info", messages["moved"].format(src=src, dst=dst))
        else:
            print(
                f"\033[1;31m{'File ' + src + ' does not exist.'.center(100)}\033[0m"
            )  # Print an error message in red
            log_message("error", messages["file_does_not_exist"].format(src=src))
    else:
        print(
            f"\033[1;33m{messages['no_operation_to_cancel'].center(100)}\033[0m"
        )  # Print a warning message in yellow
        log_message("info", messages["no_operation_to_cancel"])
        return
