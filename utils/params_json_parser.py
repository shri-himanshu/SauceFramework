import json
import os


class ParamsParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_json()

    def load_json(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")

        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get_params(self, test_file_name):
        test_name = os.path.splitext(test_file_name)[0]
        if test_name in self.data:
            return self.data[test_name]
        else:
            raise KeyError(f"No parameters found for test {test_name} in {self.file_path}")
