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
        raise ValueError("Path not provided")

    path = Path(data["path"])
    content = list((str(p) for p in path.iterdir()))

    print(json.dumps(content))


if __name__ == "__main__":
    run()
