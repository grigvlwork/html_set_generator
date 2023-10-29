import json

with open('dataset.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
counter = 0
with open('part.txt', 'w', encoding='utf-8') as f:
    for item, value in data.items():
        f.write(item)
        f.write(value)
        counter += 1
        if counter > 10000:
            break

