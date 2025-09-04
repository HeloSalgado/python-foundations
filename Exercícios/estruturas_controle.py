# Condicional
idade = 17

if idade < 18:
    print("Você é menor de idade")

elif idade >= 18 and idade < 60:
    print("Você é um adulto")

elif idade == 60:
    print("Feliz aniversário de 60 anos!")

else:
    print("Você é idoso")

# Loops
print("Números de 1 a 5 multiplicados por 2 com laço for:")
for numero in range(1, 6):
    print(numero * 2)

print("\nNúmeros de 1 a 5 multiplicados por 2 com laço while")
contador = 1
while contador <= 5:
    print(contador * 2)
    contador += 1