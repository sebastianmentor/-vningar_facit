print('Skriv in bredd och höjd på en rekangel!')
bredd = int(input('Skriv in bredden: '))
höjd = int(input('Skriv in höjd: '))

omkrets = 2*(bredd+höjd)
area = bredd*höjd

meddelande = f'En rektangel med höjden {höjd} och bredden {bredd} ' + \
            f'har en omkrets på {omkrets} och en area {area}!'

print(meddelande)