antal_inmatningar = int(input('Hur många tal önskar du lägga in: '))

lista_med_tal = []

for _ in range(antal_inmatningar):
    lista_med_tal.append(int(input('Skriv in ett tal: ')))

lista_med_jämna_tal = []
lista_med_udda_tal = []

for tal in lista_med_tal:
    if tal%2 == 0:
        lista_med_jämna_tal.append(tal)
    else:
        lista_med_udda_tal.append(tal)

#-------------------sortering av listorna-------------------------
antal_jämna_tal = len(lista_med_jämna_tal)

for start_index in range(antal_jämna_tal):
    for steg_index in range(start_index+1, antal_jämna_tal):

        if lista_med_jämna_tal[start_index] > lista_med_jämna_tal[steg_index]:

            lista_med_jämna_tal[start_index],lista_med_jämna_tal[steg_index] = lista_med_jämna_tal[steg_index], lista_med_jämna_tal[start_index]


antal_udda_tal = len(lista_med_udda_tal)

for start_index in range(antal_udda_tal):
    for steg_index in range(start_index+1, antal_udda_tal):

        if lista_med_udda_tal[start_index] > lista_med_udda_tal[steg_index]:
            
            lista_med_udda_tal[start_index],lista_med_udda_tal[steg_index] = lista_med_udda_tal[steg_index], lista_med_udda_tal[start_index]
# ----------------------------------------------------------------


for jämnt in lista_med_jämna_tal:
    print(jämnt, end=' ')

print()
for udda in lista_med_udda_tal:
    print(udda, end=' ')