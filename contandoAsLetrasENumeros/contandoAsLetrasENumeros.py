
def contando(n):
    b = str(n)
    soma = 0
    for i in range(len(b)):
        if b[i] == '1':
            alga = 2
        elif b[i] == '4':
            alga = 6
        elif b[i] == '5':
            alga = 5
        else:
            alga = 4
        soma = alga + soma
    return soma

n = int(input('Digite um número de 0 a 1000: '))
var = contando(n)
print(f'O número digitado tem {var} letras.')
