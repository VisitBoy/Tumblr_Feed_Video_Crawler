# encoding :utf-8
import json

with open("./data.json", 'rb') as f:
    str = "wget "
    data = f.read(-1)
    data = json.loads(data)
    for i in data:
        str = str + " " + i + " "

print(str)
