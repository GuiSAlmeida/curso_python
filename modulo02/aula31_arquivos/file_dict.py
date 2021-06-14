import json

dict1 = {
    'pessoa1': {
        'nome': 'Guilherme',
        'idade': 34
    },
    'pessoa2': {
        'nome': 'Andreia',
        'idade': 30
    }
}

dict1_json = json.dumps(dict1, indent=True)
print(dict1_json)

with open('pessoas.json', 'w+') as file:
    file.write(dict1_json)

with open('pessoas.json', 'r') as json_file:
    raw_json = json_file.read()
    json_to_dict = json.loads(raw_json)

print(json_to_dict)
