from typing import Optional
import json
import argparse
import os

DEFAULT_PATH = "./test-data/robot-structure-example.json"
DESCRIPTION = "Reads a JSON file and prints its contents as a formatted string."


def read_json_file(file_path: Optional[str] = None) -> str:
    """
    Reads a JSON file and returns its contents as a string.

    Args:
        file_path (Optional[str], optional): Path to the JSON file. Defaults to DEFAULT_PATH.

    Returns:
        str: Contents of the JSON file as a formatted string.
    """
    if file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, DEFAULT_PATH)

    # Read and parse the JSON file
    with open(file_path, "r") as file:
        data = json.load(file)

    # Convert the parsed JSON data to a formatted string
    return json.dumps(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("file", nargs="?", help="Path to the JSON file.")
    args = parser.parse_args()

    print(read_json_file(args.file))
