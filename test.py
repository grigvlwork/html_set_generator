import json

with open('dataset.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
counter = 0
for item, value in data.items():
    print(item)
    print(value)
    counter += 1
    if counter > 5:
        break

