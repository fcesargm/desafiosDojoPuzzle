

vet = [0 for x in range(4)]

for i in range(4):
    vet[i] = int(input(f'Digite o {i +1}º número do vetor: '))


vet.sort()
menor, *resto, maior = vet

soma = 0
for i in range (4):
    soma = vet[i] + soma

print(f'maior = {maior}, menor = {menor}, soma = {soma} ')

