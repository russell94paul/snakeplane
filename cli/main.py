# snakeplane-run CLI logic
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.loader import load_config

def main(): 
    try:
        config = load_config()
        
        if config['execution']['dry_run']:
            print("Running in dry run mode.")
        
        print(f"Using backend: {config['execution']['backend']}")
    except Exception as e:
        print(f"Error in main: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()      