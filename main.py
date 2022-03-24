import random

def calcularNumero (opt):
    if opt == 1:
        return random.randrange(1, 10)
    elif opt == 2:
        return random.randrange(1, 100)
    elif opt == 3:
        return random.randrange(1, 1000)

def encontrarNumero(n):
    encontro = False
    intentos = 0
    while (encontro == False):
        intentos = intentos + 1
        print('Ingrese numero')
        num = int(input())
        if num == n:
            encontro = True
            print('Ganaste! Te llevo ' + str(intentos) + ' intentos')
        if num < n:
            print('Un poco bajo')
        elif num > n:
            print('Un poco alto')


print('Adivina el numero')
print('Nivel 1 - De 1 a 10')
print('Nivel 2 - De 1 a 100')
print('Nivel 3 - De 1 a 1000')

opt = 0
while (opt < 1 or opt > 3):
    print('Ingrese 1, 2 o 3')
    opt = int(input())

encontrarNumero(calcularNumero(opt))