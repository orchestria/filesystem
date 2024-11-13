# /// script
# requires-python = "~=3.12"
# ///

import json
import sys
from pathlib import Path


def run():
    args = sys.argv[-1]
    data = json.loads(args)
    if "path" not in data:
        raise ValueError("path not provided")
    path = Path(data["path"])

    path.mkdir(parents=True, exist_ok=True)

    print(json.dumps({"status": "success"}))


if __name__ == "__main__":
    run()
