from __future__ import annotations

import os
import sys
import time


def my_workflow(name: str, count: int) -> dict:
    print(f"Hello, {name}!, starting a daft job")

    for i in range(count):
        print(f"processing item {i}")
        time.sleep(1)

    print(f"Thanks, {name}!, daft job completed")
    for k, v in os.environ.items():
        print(f"ENV: {k}: {v}")



    return {"results": "success"}

def main(name: str, count: int):
    return my_workflow(name, count)

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    main(name="test", count=count)

def processe_item(name: str, count: int):
    for i in range(count):
        print(f"Processing {name}'s item: {i} of {count}")
        time.sleep(1)
