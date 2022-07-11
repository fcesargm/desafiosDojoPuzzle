
def contandoosburacos(texto):
    soma = 0
    for i in range(len(texto)):
        letra = texto[i]
        if letra == 'a' or letra == 'b' or letra == 'd' or letra == 'e' or letra == 'g' or letra == 'o' or letra == 'p' or letra == 'q' or letra == 'R' or letra == 'Q' or letra == 'O' or letra == 'A' or letra == 'D':
            buracos = 1
        elif letra == 'B':
            buracos = 2
        else:
            buracos = 0
        soma = buracos + soma
    return soma

texto = input('Digite o texto desejado: ')
print(f' O número de buracos no seu texto é: {contandoosburacos(texto)}')


