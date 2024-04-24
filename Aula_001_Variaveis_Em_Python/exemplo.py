print('Hello, world!')
print('Olá, mundo!')

# Solicitar ao usuário que insira seu nome
nome = input("Digite seu nome: ")

# Solicitar ao usuário que insira o valor do seu salário
salario = float(input("Digite o valor do seu salário mensal: "))

# Solicitar ao usuário a porcentagem do bônus recebido
bonus = float(input("Digite a porcentagem do bônus recebido: "))

# Calcular o valor do bônus
valor_bonus = 1000 + salario * bonus

# Imprimir mensagem com o valor do bônus
print(f"Olá {nome}, o seu bônus foi de {valor_bonus}")
