import configparser
import os


def load_ini_and_set_env():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    ini_file_path = os.path.join(current_directory, "../startup.ini")

    if not os.path.exists(ini_file_path):
        raise FileNotFoundError(f"INI file not found at: {ini_file_path}")

    config = configparser.ConfigParser()
    config.read(ini_file_path)

    for key, value in config["DEFAULT"].items():
        os.environ[key] = value
        # Uncomment the following line to print the environment variables being set
        # print(f"Set environment variable: {key} = {value}")
