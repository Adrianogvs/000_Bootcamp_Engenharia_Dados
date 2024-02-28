print('Olá Mundo!')

# Variaveis
idade = 39
nome = "Adriano"


# Print
print(f"Minha idade é: {idade}")
print(f"Meu nome é: {nome}.")

# Soma
nova_idade = idade + 1
print(nova_idade)

# Lista
lista = [1,2,3,4,5]

# Métodos
lista_invertida = lista.reverse()

#%%
def par_impar(lista):

    pares = 0
    impares = 0

    for i in lista:
        if i % 2 == 0:
            print(f"{i} Par")
            pares += 1
        else:
            print(f"{i} Impar")
            impares += 1

    print("Total de pares:", pares)
    print("Total de ímpares:", impares)

    return pares, impares

nota = [10, 11, 55, 4, 1, 8, 87, 4, 5]
nota.sort()  # Classificar a lista antes de passá-la para a função
print(par_impar(nota))

    
# %%


#%%