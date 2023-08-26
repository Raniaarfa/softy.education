import json

with open(
    r'./JSON/person.json', 'r'
) as json_file:
    content = json_file
    person = json.loads(content)
    print(person['name'])