lista_med_tio_tal_mellan_1_och_100 = [5,11,22,23,42,45,50,66,67,99]

gissning = int(input('Gissa ett tal mellan 1 och 100: '))

if gissning in lista_med_tio_tal_mellan_1_och_100:
    print('Ha, vilken tur du har. Du gissa rätt! Det är en på 10 att det sker!')
else:
    print('Aj då, bättre lycka nästa gång!')