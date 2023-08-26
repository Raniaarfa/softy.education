import json

with open(
    r'./JSON/person.json', 'r'
) as json_file:
    content = json_file.read()
    # conversion from str to dict
    person = json.loads(content)
    print(person['name'])

#absolute path : C:\Users\hp dm1\Documents\software craft\day 4\JSON\person.json
#relative path: ./JSON/person.json