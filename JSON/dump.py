import json

pet = {
    "name":"pascal",
    "type":"Dog " ,
    "age" :4
}

with open(r"./JSON/dump.json","w") as dump_file:
    #conversion from dict to json
    dump_pet = json.dumps(pet)
    dump_file.write(dump_pet)
    print("\nfile has been created! \n")