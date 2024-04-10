import os
import pathlib
import logging
import logging.config
import time
import json
from watchdog.observers import Observer
from move_handler import MoveHandler
from utils import categorizes_files


logger = logging.getLogger(__name__)

def setup_logging() -> None:
    """Function setup logging confguration using config.json file
    """
    config_file = pathlib.Path("logging_configs/config.json")
    with open(config_file) as file:
        config = json.load(file)
    logging.config.dictConfig(config)

def get_desktop_path() -> str:
    """
    Gets desktop path
    Returns:
        (str): Desktop path
    """
    return os.path.join(os.path.expanduser("~"), "Desktop")

if __name__ == "__main__":
    setup_logging()
    desktop_path = get_desktop_path()
    file_mapping = categorizes_files()
    event_handler = MoveHandler(file_mapping, desktop_path)
    logger.info("Event handler created")
    observer = Observer()
    observer.schedule(event_handler, desktop_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt as e:
        logging.error(e)
        observer.stop()
    observer.join()
