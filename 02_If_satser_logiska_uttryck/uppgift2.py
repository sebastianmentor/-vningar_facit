tal = int(input('Skriv in ett heltal'))

if tal%2 == 0:
    print('Talet är jämnt!')
else:
    print('Talet är udda!')

#---------------------svårighetsgrad 2-----------------
tal = int(input('Skriv in ett heltal'))

if tal % 2 == 0:
    if tal % 3 == 0 and tal % 5 == 0:
        print(f'Talet är en multipel av 2*3*5. D.v.s. det finns ett tal X så att 2*3*5*X={tal}!')
    else:
        print('Talet är jämnt!')
else:
    print('Talet är udda!')