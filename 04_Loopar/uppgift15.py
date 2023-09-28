antal_inmatningar = int(input('Hur många tal önskar du lägga in: '))

lista_med_tal = []

for _ in range(antal_inmatningar):
    lista_med_tal.append(int(input('Skriv in ett tal: ')))

for swap_index in range(0,antal_inmatningar - 1,2):
    lista_med_tal[swap_index],lista_med_tal[swap_index+1]= lista_med_tal[swap_index+1],lista_med_tal[swap_index]

print(lista_med_tal)