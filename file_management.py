"""Module responsible for file management (renaming, moving)"""
import os
import shutil

class FileManagement:
    """Class responsible for file management"""
    def __init__(self, destination_dir: str, file_name: str) -> None:
        """Initializes FileManagement object.

        Args:
            destination_dir (str): File's directory path
            file_name (str): File name with its extension.
        """
        self.destination_dir = destination_dir
        self.file_name = file_name

    def create_unique_filename(self) -> str:
        """Create unique filename by adding unique number at the end of file name.

        Returns:
            str: The proper file path.
        """
        name, extension = self.file_name.split()
        path = os.path.join(self.destination_dir, self.file_name)
        counter =+ 1
        while os.path.exists(path):
            new_name = f"{name}{str(counter)}.{extension}"
            path = os.path.join(self.destination_dir, new_name)
            counter =+ 1
        return str(path)
    
    def move_file(self, source_path: str) -> None:
        """Moves file from source directory to the destination directory.

        Args:
            source_path (str): The path from file should be moved.
        """
        unique_destination_path = self.create_unique_filename()
        shutil.move(source_path, unique_destination_path)
