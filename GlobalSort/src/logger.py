import logging



def setup_logging():
    logging.basicConfig(  # Configure the logging module
        filename="file_sorter.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )


def log_message(level, message):
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
