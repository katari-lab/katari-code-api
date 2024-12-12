import configparser
import os


def load_ini_and_set_env():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    ini_file_path = os.path.join(current_directory, "../startup.ini")
    config = configparser.ConfigParser()
    config.read(ini_file_path)

    if not os.path.exists(os.path.abspath(ini_file_path)):
        raise ValueError(os.path.abspath(ini_file_path))

    for key, value in config["DEFAULT"].items():
        os.environ[key] = value
        # print(f"Set environment variable: {key} = {value}")
