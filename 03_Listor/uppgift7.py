vinstraden = [2,13,14,22,29,31,34]

print('Gissa lottoraden!!')
#...........Gissning 1................
gissning = int(input('Gissa nummeret: '))

if gissning in vinstraden:
    print('Korrekt gissat')
    vinstraden.remove(gissning)

    #...........Gissning 2................
    gissning = int(input('Gissa nummeret: '))

    if gissning in vinstraden:
        print('Korrekt gissat')
        vinstraden.remove(gissning)

        #...........Gissning 3................
        gissning = int(input('Gissa nummeret: '))

        if gissning in vinstraden:
            print('Korrekt gissat')
            vinstraden.remove(gissning)
                
            #...........Gissning 4................
            gissning = int(input('Gissa nummeret: '))

            if gissning in vinstraden:
                print('Korrekt gissat')
                vinstraden.remove(gissning)
                
                #...........Gissning 5................
                gissning = int(input('Gissa nummeret: '))

                if gissning in vinstraden:
                    print('Korrekt gissat')
                    vinstraden.remove(gissning)
                        
                    #...........Gissning 6................
                    gissning = int(input('Gissa nummeret: '))

                    if gissning in vinstraden:
                        print('Korrekt gissat')
                        vinstraden.remove(gissning)
                        
                        #...........Gissning 7................
                        gissning = int(input('Gissa nummeret: '))

                        if gissning in vinstraden:
                            print('Korrekt gissat')
                            vinstraden.remove(gissning)
                        else:
                            print('Tyvärr, ingen vinnst denna gång!!')
                    else:
                        print('Tyvärr, ingen vinnst denna gång!!')
                else:
                    print('Tyvärr, ingen vinnst denna gång!!')
            else:
                print('Tyvärr, ingen vinnst denna gång!!')
        else:
            print('Tyvärr, ingen vinnst denna gång!!')
    else:
        print('Tyvärr, ingen vinnst denna gång!!')
else:
    print('Tyvärr, ingen vinnst denna gång!!')


if len(vinstraden) == 0:
    print('Gratulerar!! Du har vunnit äran att ha alla rätt! Grattis!')


#------------------Vid användandet av loop---------------------

# vinstraden = [2,13,14,22,29,31,34]

# print('Gissa lottoraden!!')
# for _ in range(len(vinstraden)):
#     gissning = int(input('Gissa nummeret: '))

#     if gissning in vinstraden:
#         print('Korrekt gissat')
#         vinstraden.remove(gissning)
#     else:
#         print('Aj då, det va fel! Bättre lycka nästa gång!')
#         break

# if len(vinstraden) == 0:
#     print('Gratulerar!! Du har vunnit äran att ha alla rätt! Grattis!')