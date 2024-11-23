# media_alunos.py

# Recebe as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado
print(f"A média das notas é: {media:.2f}")

# Verifica se o aluno foi aprovado, reprovado ou está de recuperação
if media >= 6:
    print("Aprovado")
elif 5.0 < media < 6.0:
    print("Recuperação")
else:
    print("Reprovado")