# Dicionarios são estruturas de chave e valor

# Declarando dicionarios
function_dict = dict(name="Igor", age=25)
manual_dict = {"name": "Igor", "age": 25}

# adicionando valores
person = dict(name="Igor", age=25)
person["phone"] = "3333-3333" #{"name": "Igor", "age": 25, "phone": "3333-3333"}


# aninhando dicionarios
contacts = {
    "igor": {"sector": "a", "age": 25},
    "ju": {"sector": "b", "age": 23},
}

contacts["igor"]["sector"] # a


# iterar dicionarios

# opcao 1 
for key in contacts:
    print(key, contacts[key])

# opcao 2
for key, value in contacts.items():
    print(key, value)

