sträng_att_encoda = input('Skriv in en stränga att encoda!')
if not sträng_att_encoda:
    print('Kan inte encoda en tom sträng!')
else:
    run_kod = []
    karaktären_innan = sträng_att_encoda[0]
    antal = 1
    for karaktär in sträng_att_encoda[1:]:
        if karaktär == karaktären_innan:
            antal += 1
        else:
            run_kod.append(str(antal) + karaktären_innan)
            karaktären_innan = karaktär
            antal = 1

    run_kod.append(str(antal) + karaktären_innan)
    resultat = ''.join(run_kod)
    print('Resultatet är:', resultat)