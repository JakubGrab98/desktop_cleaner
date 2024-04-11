from pathlib import Path
import logging
from watchdog.events import FileSystemEventHandler
from file_management import FileManagement

logger = logging.getLogger(__name__)

class MoveHandler(FileSystemEventHandler):
    """Handles moving of newly created files to designated folders based on file extensions.
    """
    def __init__(self, file_mapping: dict, desktop_path: Path) -> None:
        """Initializes MoveHandler class.

        Args:
            file_mapping (dict): Mapping between folder name and files extensions.
            desktop_path (Path): Your desktop path.
        """
        self.file_mapping = file_mapping
        self.desktop_path = desktop_path
    
    def on_created(self, event):
        """Checks and moves the file when it is created on desktop.
        """
        logger.info(f"Event type: {event.event_type} path: {event.src_path}")
        source_path = Path(event.src_path)
        file_extension = source_path.suffix.lower()

        for folder, extensions in self.file_mapping.items():
            if file_extension in extensions:
                target_folder = self.desktop_path.joinpath(folder)
                try:
                    file_manager = FileManagement(target_folder, source_path.name)
                    file_manager.move_file(source_path)
                except Exception as e:
                    logger.error(f"Error moving file {source_path}: {e}")
