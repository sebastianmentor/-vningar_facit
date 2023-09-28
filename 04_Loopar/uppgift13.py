antal_inmatningar = int(input('Hur många tal önskar du lägga in: '))

lista_med_tal = []

for _ in range(antal_inmatningar):
    lista_med_tal.append(int(input('Skriv in ett tal: ')))

# listan är inte tom
if lista_med_tal:
    minsta_talet = lista_med_tal[0]
    största_talet = lista_med_tal[0]

    for tal in lista_med_tal:
        if tal < minsta_talet: minsta_talet = tal
        if tal > största_talet: största_talet = tal

print(f'Största differansen är mellan {minsta_talet} och {största_talet} vilket är {största_talet-minsta_talet}')