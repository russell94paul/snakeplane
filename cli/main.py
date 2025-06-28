# snakeplane-run CLI logic
from config.loader import load_config

def main():
    config = load_config()
    
    if config['execution']['dry_run']:
        print("Running in dry run mode.")
    
    print(f"Using backend: {config['execution']['backend']}")