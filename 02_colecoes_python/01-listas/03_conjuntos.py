# Funções

# SET()  remove elementos duplicados e devolve um dicionario

set([1, 2, 3, 1, 3, 4]) # {"1", "2", "3", "4"}

# Conjuntos não suportam indexação ou fatiamento, portanto, para acessar os valores é necessário converter para lista

nums = {1, 2, 3, 4}

nums = list(nums)

nums[0] # 1

# É possível iterar conjuntos

cars =  {"gol", "celta", "palio"}

for i, car in enumerate(cars):
    print(f"{i}: {car}")


# Operações com conjunto 

a = {1, 2, 3}
b = {2, 3, 4}

a.union(b) # {1, 2, 3, 4}
a.intersection(b) # {2, 3}
a.difference(b) # {1}
a.symmetric_difference(b) # {1, 4}      # apenas em A + apenas em B (desconsidera a intersecção)

# Lembre-se dos diagramas de Venn

venn_a = {1, 2, 3}
venn_b = {4, 1, 2, 5, 6, 3}

venn_a.issubset(venn_b) # True    # Tudo que está em A, está em B
venn_b.issubset(venn_a) # False   # Mas nem tudo que está em B, está em A

venn_a.issuperset(venn_b) # False   # Nem tudo que está em B, está em A
venn_b.issuperset(venn_a) # True   # Mas tudo que está em A, está em B

venn_a.isdisjoint(venn_b) # False    # Há intersecção, portanto "isdisjoint = false"

venn_a.add(23) # {1, 2, 3, 23}

