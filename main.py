# missão 1 - criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

# nota1 = 5

# if nota1 >= 6:
#   print("Aluno aprovado")
# else:
#   print("Aluno reprovado")

# # missão 2 - criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

# idade = int(input("Qual a sua idade? "))

# if idade >= 16:
#   print("Você pode votar")
# else:
#   print("Você não pode votar")

# # missão 3 - criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:
# # - A (90-100) – "Parabéns, você tirou A!"
# # - B (80-89) – "Muito bem, você tirou B."
# # - C (70-79) – "Bom trabalho, você tirou C."
# # - D (60-69) – "Fique atento, você tirou D."
# # - F (menos de 60) – "Estude um pouco mais, você tirou F."

# nota2 = int(input("Insira sua nota: "))

# if nota2 >= 90 and nota2 <= 100:
#   print("Parabéns, você tirou A!")
# elif nota2 <= 89 and nota2 >= 80:
#   print("Muito bem, você tirou B.")
# elif nota2 <= 79 and nota2 >= 70:
#   print("Bom trabalho, você tirou C.")
# elif nota2 <= 69 and nota2 >= 60:
#   print("Fique atento, você tirou D.")
# elif nota2 < 60:
#   print("Estude um pouco mais, você tirou F.")
# else:
#   print("Numero fora do escopo")

# # missão 5 - crie um programa que peça dois números ao usuário e exiba a soma deles.
# val1 =  int(input("Insira um numero: "))
# val2 =  int(input("Insira outro numero: "))
# print(f"{val1} + {val2} = {val1 + val2}")

# # missão 5 - crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".
# senha = input("qual a senha? ")
# if senha == "Python123":
#   print("Senha correta")
# else:
#   print("Senha incorreta")

# missão 6 - Exiba os números de 1 a 10 usando um loop while. 
i = 0
while i < 10:
  i += 1
  print(f"{i}")

# missão 7 - Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente. Isso ajudará a colocar tudo em ordem corretamente!  

lista = [8, 3, 10, 1, 5]
lista.sort()
print(lista)

# missão 8 - crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.  
tupla = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")
print(f"{tupla[0]} e {tupla[-1]}")

# missão 9 - Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
def dobro(num):
  print(f"O dobro de {num} é {num * 2}")

dobro(5)

# missão 10 - crie uma função que receba um nome e diga quantas letras esse nome tem.
def contar_letras(nome):
  print(f"O nome {nome} tem {len(nome)} letras")
contar_letras("Ana")