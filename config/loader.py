# Python loader to access config
import yaml
import os

def load_config(path=None):
    default_path = os.path.join(os.path.dirname(__file__), "defaults.yaml")
    config_path = path or default_path
    with open(config_path, "r") as f:
        return yaml.safe_load(f)