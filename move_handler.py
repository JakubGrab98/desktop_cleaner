import os
import logging
from watchdog.events import FileSystemEventHandler
from file_management import FileManagement

logger = logging.getLogger(__name__)

class MoveHandler(FileSystemEventHandler):
    def __init__(self, file_mapping: dict, desktop_path: str) -> None:
        self.file_mapping = file_mapping
        self.desktop_path = desktop_path
    
    def on_created(self, event):
        logger.info(f"Event type: {event.event_type} path: {event.src_path}")
        source_path = event.src_path
        file_name = os.path.basename(source_path)
        ext = os.path.splitext(file_name)[1].lower()
        for folder, extensions in self.file_mapping.items():
            if ext in extensions:
                target_folder = os.path.join(self.desktop_path, folder)
                file_manager = FileManagement(target_folder, file_name)
                file_manager.move_file(source_path)
