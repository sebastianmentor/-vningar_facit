tal = int(input('Skriv in ett naturligt tal: '))
tal_kopia = tal
fakultet = 1
while tal_kopia > 0:
    fakultet *= tal_kopia
    tal_kopia-=1

if fakultet >= 1 and tal > 0:
    print(f'{tal}! av är {fakultet}!')