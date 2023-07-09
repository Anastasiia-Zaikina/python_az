from homework13.abstract_writer import Writer


class TxtWriter(Writer):
    def __init__(self, file_path: str, mode: str):
        self.file_path = file_path
        self.mode = mode

    def write_to_file(self, data):
        with open(self.file_path, mode=self.mode) as file:
            file.write(data)
