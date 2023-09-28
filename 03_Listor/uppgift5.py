min_lista_med_favoritdjur = ['hund', 'katt', 'kanin', 'häst']

print('Skriv in tre djur du gillar!')
djur1 = input('Skriv in första favoritdjuret: ').lower()
djur2 = input('Skriv in andra favoritdjuret: ').lower()
djur3 = input('Skriv in tredje favoritdjuret: ').lower()

antal_djur_vi_gillar_tillsammans = 0

if djur1 in min_lista_med_favoritdjur:
    antal_djur_vi_gillar_tillsammans +=1
if djur2 in min_lista_med_favoritdjur:
    antal_djur_vi_gillar_tillsammans +=1
if djur3 in min_lista_med_favoritdjur:
    antal_djur_vi_gillar_tillsammans +=1

print(f'Vi har {antal_djur_vi_gillar_tillsammans} st gemensamma djur vi gillar!')

#----------------Lite klurigare-------------------------------

# min_lista_med_favoritdjur = ['hund', 'katt', 'kanin', 'häst']

# djur = input('Skriv in tre djur du gillar!: ').lower().split()

# antal_djur_vi_gillar_tillsammans = 0

# if djur[0] in min_lista_med_favoritdjur:
#     antal_djur_vi_gillar_tillsammans +=1
# if djur[1] in min_lista_med_favoritdjur:
#     antal_djur_vi_gillar_tillsammans +=1
# if djur[2] in min_lista_med_favoritdjur:
#     antal_djur_vi_gillar_tillsammans +=1

# print(f'Vi har {antal_djur_vi_gillar_tillsammans} st gemensamma djur vi gillar!')