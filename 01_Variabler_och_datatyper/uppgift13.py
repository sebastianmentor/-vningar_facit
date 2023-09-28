print('Skriv in antal veckor, dagar och timmar!')
veckor = int(input('Skriv antal veckor: '))
dagar = int(input('Skriv antal dagar: '))
timmar = int(input('Skriv antal timmar: '))

totalt_antal_timmar = (veckor*7+dagar)*24 + timmar

print('Totalt antal timmar är', totalt_antal_timmar )

print(f'Totalt antal dagar är {totalt_antal_timmar/24:.1f}')
print(f'Totalt antal veckor är {totalt_antal_timmar/(24*7):.1f}')
print(f'Totalt antal år är {totalt_antal_timmar/(24*365):.1f}')