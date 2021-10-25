import json

with open("menu.json",encoding = 'utf8') as file:
    data = json.load(file)
print(data)