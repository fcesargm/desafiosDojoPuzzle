
n = int(input('Qual número você deseja verificar se é primo? '))

soma = 0

for i in range(2,n):
    if n % i == 0:
        mult = i
        print(n, 'é múltiplo de', mult)
        soma += 1

if soma == 0:
    print('O número ', n, ' é primo!')
else:
    print('O número ', n, ' possui ', soma, ' divisores')