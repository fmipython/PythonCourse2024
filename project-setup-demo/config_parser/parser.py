import yaml


class ConfigParser:
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file
        self.config = {}

    def parse(self) -> None:
        with open(self.config_file, "r") as f:
            loaded = yaml.load(f, Loader=yaml.CLoader)
            self.config = loaded


if __name__ == "__main__":
    # for testing purposes
    parser = ConfigParser("../configs/ai-easy.yaml")
    parser.parse()
    print(parser.config)
