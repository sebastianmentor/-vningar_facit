print('Skriv in tre nummer!')
num1 = int(input('Skriv in första nummeret: '))
num2 = int(input('Skriv in andra nummeret: '))
num3 = int(input('Skriv in tredje nummeret: '))

lista_med_tre_nummer = [num1,num2,num3]

max_nummer = max(lista_med_tre_nummer)
min_nummer = min(lista_med_tre_nummer)

lista_med_tre_nummer.remove(max_nummer)
lista_med_tre_nummer.remove(min_nummer)

print(f'Medianen är', lista_med_tre_nummer[0])

