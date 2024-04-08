import os

class FileManagement:
    def __init__(self, destination_dir: str, file_name: str) -> None:
        self.destination_dir = destination_dir
        self.file_name = file_name
        self.full_path = os.path.join(destination_dir, file_name)

    def create_unique_filename(self):
        name, extension = self.file_name.split()
        counter = 1

        while os.path.exists(self.full_path):
            pass
