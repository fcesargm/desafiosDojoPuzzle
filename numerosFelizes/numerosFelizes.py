try:
    def numfeliz(n):
        b = str(n)
        soma = 0
        for i in range(len(b)):
            var = int(b[i])
            soma += var ** 2
        if soma >= 2:
            return numfeliz(soma)
        else:
            return soma


    n = int(input('Digite o número que deseja verificar se é feliz: '))
    var = numfeliz(n)
    if var == 1:
        print('O número informado é um número Feliz!')
except:
    print('O número informado não é um número feliz =(')
