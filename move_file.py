# /// script
# requires-python = "~=3.12"
# ///
import json
import shutil
import sys


def move_file():
    args = sys.argv[-1]
    data = json.loads(args)
    if "source" not in data:
        raise ValueError("Source path not provided")
    if "target" not in data:
        raise ValueError("Target path not provided")

    shutil.move(data["source"], data["target"])

    print(json.dumps({"status": "success"}))


if __name__ == "__main__":
    move_file()
