
contacts = {
    "igor": {"sector": "a", "age": 25},
    "ju": {"sector": "b", "age": 23},
}

# GET

contacts.get("key") # None          #Se não encontrar "key", retorna "None"
contacts.get("key", {}) # {}        # segundo argumento é um valor padrão caso não encontre "key"
contacts.get("igor", {}) # "igor": {"sector": "a", "age": 25}

# ITEMS 

# Devolve tuplas com cada item
print(contacts.items()) # dict_items([('igor', {'sector': 'a', 'age': 25}), ('ju', {'sector': 'b', 'age': 23})]) 


# KEYS 

contacts.keys() # dict_key(['igor', 'ju'])