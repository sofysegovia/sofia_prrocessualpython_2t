aniversario = 11
contador = 0 

while contador <= 100:
    multiplicacao = contador * aniversario
    contador+= 1
    if multiplicacao > 1000:
        print(f"O número {multiplicacao} é maior que 1000!")
    print(multiplicacao)
