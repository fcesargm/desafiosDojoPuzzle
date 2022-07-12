

# vetor: [int] = [0 for x in range(4)]
# for i in range(4):
#     num = int(input(f'Digite o {i + 1}º número do vetor: '))
#     vetor[i] = num
#
# maior = vetor[0]
# for i in range(1, 4):
#     if vetor[i] > maior:
#         maior = vetor[i]
#
# menor = vetor[0]
# for i in range(1, 4):
#     if vetor[i] < menor:
#         menor = vetor[i]
#
# soma = 0
# for i in range(4):
#     soma += vetor[i]
#
# print(f' O maior valor é {maior}, o menor valor é {menor} e a soma de todos os valores é {soma}')

vetor: [int] = [0 for x in range(4)]
for i in range(4):
    num = int(input(f'Digite o {i + 1}º número do vetor: '))
    vetor[i] = num

vetor.sort()
menor, *resto, maior = vetor

soma = 0
for i in range(4):
    soma += vetor[i]

print(f'O maior valor é {maior}, o menor valor é {menor} e a soma de todos os valores é {soma}')






