
vetor = [30, 54, 89, 1]

maior = vetor[0]
for i in range(4):
    if vetor[i] > maior:
        maior = vetor[i]

menor = vetor[0]
for i in range(4):
    if vetor[i] < menor:
        menor = vetor[i]

soma = 0
for i in range(4):
    soma = vetor[i]+ soma

print(f'soma = {soma}, maior = {maior}, menor ={menor}')

