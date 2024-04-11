import pytest
from pathlib import Path
from file_management import FileManagement

@pytest.fixture
def temp_dirs(tmp_path):
    source_dir = tmp_path.joinpath("source")
    dest_dir = tmp_path.joinpath("dest")
    source_dir.mkdir()
    dest_dir.mkdir()
    return source_dir, dest_dir

@pytest.fixture
def file_manager(tmp_path):
    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()
    return FileManagement(dest_dir, "test_file.txt")

def test_move_file_success(temp_dirs):
    source_dir, dest_dir = temp_dirs
    test_file = source_dir.joinpath("test_file.txt")
    test_file.write_text("Test content")
    
    fm = FileManagement(dest_dir, test_file.name)
    fm.move_file(test_file)
    
    assert (dest_dir.joinpath(test_file.name)).exists()
    assert not test_file.exists()

def test_create_unique_filename_no_conflict(file_manager):
    expected_path = Path(file_manager.destination_dir.joinpath("test_file.txt"))

    assert file_manager.create_unique_filename() == expected_path

def test_create_unique_filename_with_conflict(file_manager):
    existing_file = Path(file_manager.destination_dir.joinpath("test_file.txt"))
    existing_file.touch()

    expected_path = Path(file_manager.destination_dir.joinpath("test_file1.txt"))

    assert file_manager.create_unique_filename() == expected_path

def test_create_unique_filename_multiple_conflict(file_manager):
    Path(file_manager.destination_dir.joinpath("test_file.txt")).touch()
    Path(file_manager.destination_dir.joinpath("test_file1.txt")).touch()
    Path(file_manager.destination_dir.joinpath("test_file2.txt")).touch()


    expected_path = Path(file_manager.destination_dir.joinpath("test_file3.txt"))

    assert file_manager.create_unique_filename() == expected_path
