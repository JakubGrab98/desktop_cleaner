import pathlib
import logging
import logging.config
import time
import json
from utils import categorizes_files
from move_handler import MoveHandler
from watchdog.observers import Observer


logger = logging.getLogger(__name__)

def setup_logging():
    config_file = pathlib.Path("logging_configs/config.json")
    with open(config_file) as file:
        config = json.load(file)
    logging.config.dictConfig(config)


if __name__ == "__main__":
    setup_logging()
    desktop_path = r"C:\Users\kubag\Desktop"
    file_mapping = categorizes_files()
    event_handler = MoveHandler(file_mapping, desktop_path)
    logger.info("Event handler created")
    observer = Observer()
    observer.schedule(event_handler, desktop_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()