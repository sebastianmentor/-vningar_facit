tal = int(input('Skriv in ett naturligt tal: '))
tal_kopia = tal
summa = 0
while tal_kopia > 0:
    summa += tal_kopia
    tal_kopia-=1

if summa != 0:
    print(f'Summan av alla talen från 1 upp till {tal} är {summa}!')