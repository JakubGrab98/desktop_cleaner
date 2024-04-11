from pathlib import Path
import shutil
import logging

logger = logging.getLogger(__name__)

class FileManagement:
    """Class responsible for file management."""
    def __init__(self, destination_dir: Path, file_name: str) -> None:
        """Initializes FileManagement object.

        Args:
            destination_dir (str): File's directory path.
            file_name (str): File name with its extension.
        """
        self.destination_dir = self.check_directory(destination_dir)
        self.file_name = file_name

    @staticmethod
    def check_directory(directory: Path) -> Path:
        """
        Function checks if directory exists and make directory when not.
        Args:
            directory (Path): Directory path to be checked or maked.

        Returns:
            Path: Directory path.
        """
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            logger.info(f"{directory} was created!")
        return directory

    def create_unique_filename(self) -> Path:
        """Create unique filename by adding unique number at the end of file name.

        Returns:
            Path: The proper file path.
        """
        destination_path = self.destination_dir.joinpath(self.file_name)
        extension = destination_path.suffix
        counter = 1
        while destination_path.exists():
            name = destination_path.stem
            new_name = f"{name}{str(counter)}{extension}"
            destination_path = self.destination_dir.joinpath(new_name)
            counter += 1
        return destination_path
    
    def move_file(self, source_path: Path) -> None:
        """Moves file from source directory to the destination directory.

        Args:
            source_path (Path): The path from file should be moved.
        """
        unique_destination_path = self.create_unique_filename()
        try:
            shutil.move(source_path, unique_destination_path)
            logger.info(f"File was saved in {unique_destination_path}.")
        except Exception as e:
            logger.error(f"Error moving file: {e}.")
