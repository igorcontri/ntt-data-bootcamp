def show_poem(date, *args, **kwargs):

    text = "\n".join(args)
    data = "\n".join([f"{key.title()}: {value}" for key, value in kwargs.items()])
    message = f"{date}\n\n{text}\n\n{data}"

    print(message)

show_poem(
    "12/07/2024",
    "Somebody save me",
    "Me from myself",
    "I've spent so long livin' in hell",
    "They say my lifestyle is bad for my health",
    "It's the only thing that seems to help",
    author="Eminem",
    song="Somebody Save Me"
)

#Este exemplo é uma combinação de tudo

# date é um parametro posicional
# *args é um parametro obrigatório que devolve tuplas (*args é um nome convencional, poderia ser "*tomate")
# **kwargs é um parametro obrigatório que devolve dicionários (*kwargs tbm é convencional, poderia ser "abacate")

# No caso da chamada da função o a primeira string, é um argumento posicional que será atribuida ao parametro "date"
# tudo que vier na sequecia será atribuido ao parametro *args, ou seja, fará tupla de todas as strings separadas por virgula na sequencia
# Por fim, quando entra argumentos com chave e valor (author="Eminem"), estes caem no parametro **kwargs.