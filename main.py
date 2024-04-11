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
    """Function setups logging confguration using config.json file.
    """
    config_file = pathlib.Path("logging_configs/config.json")
    try:
        with open(config_file) as file:
            config = json.load(file)
        logging.config.dictConfig(config)
    except FileNotFoundError:
        logging.error("Logging configuration file not found.")
    except json.JSONDecodeError:
        logger.error("Invalid JSON in the logging configuration file.")

def get_desktop_path() -> pathlib.Path:
    """
    Gets desktop path
    Returns:
        Path: Desktop path
    """
    return pathlib.Path.home().joinpath("Desktop")

if __name__ == "__main__":
    setup_logging()
    try:
        desktop_path = get_desktop_path()
        file_mapping = categorizes_files()
        event_handler = MoveHandler(file_mapping, desktop_path)
        logger.info("Event handler created.")
        observer = Observer()
        observer.schedule(event_handler, desktop_path, recursive=False)
        observer.start()
        logger.info("Observer starter. Monitoring desktop for changes.")
    except Exception as e:
        logger.error(f"Failed to start observer due to error: {e}.")
    else:
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt as e:
            logging.error(e)
            observer.stop()
        observer.join()
