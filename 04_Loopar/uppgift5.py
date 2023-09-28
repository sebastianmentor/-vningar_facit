fib_n = int(input('Skriv in ett tal: '))

fib_n_minus_2 = 0
fib_n_minus_1 = 1


if fib_n < 0:
    print('Odefinerat')
elif fib_n == 0:
    print(0)
elif fib_n == 1:
    print(1)
else:
    print(0,1, sep=', ',end=', ')
    steg = 2
    while steg < fib_n:
        new_fib = fib_n_minus_1 + fib_n_minus_2
        print(new_fib, end= ', ')
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = new_fib
        steg +=1


