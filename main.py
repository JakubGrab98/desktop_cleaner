import os
import time
from utils import categorizes_files
from move_handler import MoveHandler
from watchdog.observers import Observer


if __name__ == "__main__":
    desktop_path = r"C:\Users\kubag\Desktop"
    file_mapping = categorizes_files()
    event_handler = MoveHandler(file_mapping, desktop_path)
    observer = Observer()
    observer.schedule(event_handler, desktop_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()