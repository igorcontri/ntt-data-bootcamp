class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


print("===== inicio ======")
aluno_1 = Estudante("Igor", 1)
aluno_2 = Estudante("Ju", 2)
mostrar_valores(aluno_1, aluno_2)

print("===== geral ======")
# alterando valor para todos
Estudante.escola = "Python"
# O proximo estudante recebe a nova escola
aluno_3 = Estudante("Ciri", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

# alterando valor especifico
print("===== especifico ======")
aluno_1.escola = "Js"
mostrar_valores(aluno_1, aluno_2, aluno_3)