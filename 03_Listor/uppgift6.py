mening = input('Skriv in en mening: ')

if mening != '':
    lista_med_ord = list(mening.strip().split())
    print('Antal ord i meningen är', len(lista_med_ord))


#------------Lite klurigare------------------------
# mening = input('Skriv in en mening: ')

# if mening != '':
#     lista_med_ord = list(mening.strip().split())
#     print('Antal ord i meningen är', len(lista_med_ord))
#     if mening[0].isalpha() and mening[0]==mening[0].upper and mening.endswith('.'):
#         print('Korrekt skrivet!!')
