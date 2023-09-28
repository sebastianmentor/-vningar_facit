mening = input('Skriv in en mening!')


if mening == '':
    print('Jaha, skit i det då!')
else:
    if mening.strip() == '':
        print('Spacit!!!')
    else:
        if mening == mening.upper():
            print('BIG LETTERS!')
            
    if mening.startswith('He'):
        print('He........!')
    if mening.endswith('.'):
        print('Korrekt avslut!')
    if len(mening) >= 24:
        print('Oj, du va en produktiv jäkel!')
    if mening[0] == mening[-1]:
        print(mening[1:-1])
    if mening.count('a') >= 3 or mening.count('b') >= 4 or mening.count('c') >= 2:
        print('aaa eller bbbb eller ccc min kära användare!')