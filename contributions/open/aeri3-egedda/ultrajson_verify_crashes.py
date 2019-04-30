import os
import ujson

path = "bugs/ultrajson/"

for f in os.listdir(path):
    try:
        with open(path + f + "/input.json", "rb") as f:
            try:
                ujson.loads(f.read())
            except ValueError:
                pass
    except FileNotFoundError:
        pass
