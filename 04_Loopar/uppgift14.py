antal_tal = int(input('Hur många tal önskar du lägga in: '))

lista_med_tal = []

for _ in range(antal_tal):
    lista_med_tal.append(int(input('Skriv in ett tal: ')))

index = 0 # vi börjar med att kolla alla dubletter av listan[0]
titta_i_resten_av_listan = antal_tal - 1 # vi tittar igenom listan[1:] 

while True:
    # 
    if titta_i_resten_av_listan < index:
        break
    
    steg_index = index + 1

    while titta_i_resten_av_listan >= steg_index:

        if lista_med_tal[index] == lista_med_tal[steg_index]:
            titta_i_resten_av_listan-=1
            lista_med_tal.pop(steg_index)
            
        else:
            steg_index += 1
    index +=1
    

print(lista_med_tal)
