class ConfigReader:
    def __init__(self):
        self.config_data = self._read_config_file(
            "D:\\Automation\\automationQAPython\\AQA_python\\project.properties"
        )

    @staticmethod
    def _read_config_file(file_path):
        config_data = {}
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                config_data[key] = value
        return config_data

    def get_base_url(self):
        return self.config_data.get("base_url", "")
