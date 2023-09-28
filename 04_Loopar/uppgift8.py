n = int(input('Skriv in ett positivt heltal: '))

steg = 0
while n != 1:
    print(n)
    if n % 2 == 0:
        # n /= 2
        n = n//2
    else:
        n = 3*n + 1
    steg += 1

print(f"Antal steg är {steg}")