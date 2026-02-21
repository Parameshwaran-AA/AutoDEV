import os


class FileTool:

    def write_file(self, path: str, content: str):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)

    def read_file(self, path: str):
        with open(path, "r") as f:
            return f.read()
