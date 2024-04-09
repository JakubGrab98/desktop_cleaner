def categorizes_files() -> dict:
    """Function collects mapping between file extensions and destination folder.

    Returns:
        dict: Returns folder mapping as dictionary.
    """
    file_mapping = {
        "documents": [
            ".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx",
        ],
        "images": [
            ".jpg", ".jpeg",
        ],
        "videos": [
            ".webm", ".mpg", ".mp2", ".mpeg", ".mpv", ".mp4", ".mp4v", ".m4v",".wmv",
        ],
    }
    return file_mapping
