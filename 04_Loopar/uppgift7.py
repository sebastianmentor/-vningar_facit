import math

N = int(input('Skriv in ett posetivt heltal: '))

if N > 0:
    print(2)
    for i in range(3,N):
        övre_gräns = int(math.sqrt(i)+1)
        is_prime = True
        for j in range(2,övre_gräns):
            if i%j ==0:
                is_prime = False
                break

        if is_prime: print(i)