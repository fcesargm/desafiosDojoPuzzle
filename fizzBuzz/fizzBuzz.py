
def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else:
        return n

numero = 1
var = fizzBuzz(numero)
for i in range(100):
    var = fizzBuzz(numero)
    print(var)
    numero += 1

