# /// script
# requires-python = "~=3.12"
# dependencies = ["rich"]
# ///
import json
import sys
from pathlib import Path

import rich.prompt


def remove_files():
    args = sys.argv[-1]
    data = json.loads(args)
    if "files" not in data:
        raise ValueError("Files not provided")

    files = [Path(f) for f in data["files"]]

    if not files:
        print(json.dumps({"status": "success"}))
        return

    message = "Are you sure you want to remove the following files?"
    for f in files:
        message += f"\n- {f}"
    confirm = rich.prompt.Confirm()
    if confirm.ask(prompt=message, default=False):
        for f in files:
            f.unlink(missing_ok=True)
        print(json.dumps({"status": "success"}))
        return

    print(json.dumps({"status": "cancelled"}))


if __name__ == "__main__":
    remove_files()
