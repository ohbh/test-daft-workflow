from __future__ import annotations

import os
import time



def my_workflow(name: str) -> dict:
    print(f"Hello, {name}!, starting a daft job")

    for i in range(100):
        print(f"processing item {i}")
        time.sleep(1)

    print(f"Thanks, {name}!, daft job completed")
    for k, v in os.environ.items():
        print(f"ENV: {k}: {v}")



    return {"results": "success"}

def main(name: str):
    return my_workflow(name)

if __name__ == "__main__":
    main(name="test")

def processe_item(name: str, count: int):
    for i in range(count):
        print(f"Processing {name}'s item: {i} of {count}")
        time.sleep(1)
