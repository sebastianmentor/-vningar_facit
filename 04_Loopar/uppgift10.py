n = int(input('Skriv in tal: '))
resultat = []
for i in range(n):
    rad = (i+1)*[None]
    rad[0], rad[-1] = 1, 1
    for j in range(1, len(rad) - 1):
        rad[j] = resultat[i - 1][j - 1] + resultat[i - 1][j]
    resultat.append(rad)

# print(resultat)
antal_karaktärer = ''
for element in resultat[-1]:
    antal_karaktärer += str(element)+' '

width = len(antal_karaktärer)
for rad in resultat:
    pasc_row_str = ''
    for element in rad:
        pasc_row_str+= str(element) + ' '
    print(pasc_row_str.center(width))