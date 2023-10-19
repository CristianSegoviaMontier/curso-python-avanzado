def fibonacci(n):
    fib_serie = [0, 1]
    while len(fib_serie) < n:
        next_num = fib_serie[-1] + fib_serie[-2]
        fib_serie.append(next_num)
    return fib_serie


if __name__ == '__main__':
    n = int(input('Ingrese cantidad de numeros en la serie :'))
    print('La serie de finocci solicitada es : \n', fibonacci(n))
