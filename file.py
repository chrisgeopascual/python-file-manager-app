from pathlib import Path

class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def create(self):
        p = Path(self.file_name)
        if p.exists():
             return f"'{self.file_name}' already exists"
        p.write_text("| Name | Username | Password |")
        return f"Created {self.file_name}"

    def search(self):
        p = Path(self.file_name)
        if not p.exists():
            return f"'{self.file_name}' not found"
        return p.read_text()

    def update(self, new_row: str):
        p = Path(self.file_name)
        if not p.exists():
            return f"'{self.file_name}' not found, User Created instead"
        existing = p.read_text()

        p.write_text(existing + "\n" + new_row)
        return f"Updated {self.file_name}"
        
    def delete(self):
        p = Path(self.file_name)
        if not p.exists():
            return f"'{self.file_name}' not found"
        p.unlink()
        return f"Deleted {self.file_name}"
    