from __future__ import annotations

import os
import pathlib
from re import S
import time

import daft
from daft.functions.ai import embed_text


def mkdir() -> str:
    desktop = os.path.join(pathlib.Path("~").expanduser(), "Desktop")
    timestamp = str(int(time.time()))
    path = os.path.join(desktop, timestamp)
    pathlib.Path(path).mkdir(exist_ok=True, parents=True)
    return path


def my_workflow(name: str) -> dict:
    print(f"Hello, {name}!, starting a daft job")

    print(f"Thanks, {name}!, daft job completed")
    processe_item(name, 10)

    return {"results": "success"}

def main(name: str):
    my_workflow(name)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, required=True, help="Name to use in workflow")
    args = parser.parse_args()
    main(name=args.name)

def processe_item(name: str, count: int):
    for i in range(count):
        print(f"Processing {name}'s item: {i} of {count}")
        time.sleep(1)
