FAV1 = 'fil'
FAV2 = 'ägg'
FAV3 = 'bacon'
FAV4 = 'ostmacka'

print('Skriv in 3 saker du åt till frukost!')
mat1 = input('Första saken: ').lower()
mat2 = input('Andra saken: ').lower()
mat3 = input('Tredje saken: ').lower()

print(f'Till frukost år du {mat1},{mat2} och {mat3}. Låter gott!')

if FAV1 in mat1 or FAV1 in mat2 or FAV1 in mat3:
    print('Vi båda gillar', FAV1)

if FAV2 in mat1 or FAV2 in mat2 or FAV2 in mat3:
    print('Vi båda gillar', FAV2)

if FAV3 in mat1 or FAV3 in mat2 or FAV3 in mat3:
    print('Vi båda gillar', FAV3)

if FAV4 in mat1 or FAV4 in mat2 or FAV4 in mat3:
    print('Vi båda gillar', FAV4)