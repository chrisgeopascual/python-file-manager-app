from file_manager_app import process_file
from file import File

def test_process_file_choice_1_is_still_running(tmp_path):
    target = tmp_path / "test.txt"
    assert process_file("1", str(target)) is True

def test_process_file_choice_5_is_not_running(tmp_path):
    target = tmp_path / "test.txt"
    assert process_file("5", str(target)) is False

def test_process_file_choice_4_delete_still_running(tmp_path):
    target = tmp_path / "test.txt"
    target.write_text("some content")
    assert process_file("4", str(target)) is True
    assert not target.exists()

def test_process_file_choice_is_not_in_range_still_running(tmp_path):
    target = tmp_path / "test.txt"
    assert process_file("99", str(target)) is True

def test_process_file_choice_is_not_digit_still_running(tmp_path):
    target = tmp_path / "test.txt"
    assert process_file("99", str(target)) is True

def test_create_new_file(tmp_path):
    target = tmp_path / "users.txt"
    f = File(str(target))
    result = f.create()
    assert "Created" in result
    assert target.read_text() == "| Name | Username | Password |"

def test_create_existing_file_does_not_overwrite(tmp_path):
    target = tmp_path / "users.txt"
    target.write_text("original")
    f = File(str(target))
    result = f.create()
    assert "already exists" in result
    assert target.read_text() == "original"

def test_update_appends_not_overwrites(tmp_path):
    target = tmp_path / "users.txt"
    target.write_text("| Name | Username | Password |")
    f = File(str(target))
    f.update("| John Doe | John | admin123 |")
    content = target.read_text()
    assert "| Name | Username | Password |" in content
    assert "| John Doe | John | admin123 |" in content

def test_update_missing_file(tmp_path):
    target = tmp_path / "ghost.txt"
    f = File(str(target))
    result = f.update("| John Doe | John | admin123 |")
    assert "not found" in result
    assert not target.exists()

def test_delete_existing_file(tmp_path):
    target = tmp_path / "users.txt"
    target.write_text("content")
    f = File(str(target))
    result = f.delete()
    assert "Deleted" in result
    assert not target.exists()

def test_delete_missing_file(tmp_path):
    target = tmp_path / "ghost.txt"
    f = File(str(target))
    result = f.delete()
    assert "not found" in result