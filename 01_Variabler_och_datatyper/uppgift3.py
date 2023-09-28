#---------------version 1----------------------
print('Låt mig få addera två tal åt dig!')
num1 = input('Skriv in det första talet: ')
num2 = input('Skriv in det andra talet: ')

print('Summan blir', num1+num2)



#---------------svårighetsgrad 2----------------------
# print('Låt mig få addera två tal åt dig!')
# num1 = int(input('Skriv in det första talet: '))
# num2 = int(input('Skriv in det andra talet: '))

# print(f'Summan av {num1} + {num2} är {num1+num2}!')

#---------------svårighetsgrad 3+----------------------
# Finns flera sätt att lösa detta på
# print('Låt mig få addera två tal åt dig!')
# num1 = input('Skriv in det första talet: ')
# num2 = input('Skriv in det andra talet: ')

# # Båda talen är tal
# if num1.isdigit() and num2.isdigit():
#     print(f'Summan av {num1} + {num2} är {int(num1)+int(num2)}!')
# # Båda talen är inte tal
# elif (not num1.isdigit()) and (not num2.isdigit()):
#     print(f'Både {num1} och {num2} är inte tal')
# # Annars om num1 är ett giltligt tal
# elif num1.isdigit():
#     print(f'Andra inputen {num2} är inte ett tal!')
# # Annars är num2 ett tal men num1 inte!!
# else:
#     print(f'Första inputen {num1} är inte ett tal!!')
    
#---------------svårighetsgrad 3+----------------------
# Finns flera sätt att lösa detta på
# print('Låt mig få addera två tal åt dig!')
# num1 = input('Skriv in det första talet: ')
# num2 = input('Skriv in det andra talet: ')

# num1_är_ett_tal = num1.isdigit()
# num2_är_ett_tal = num2.isdigit()

# if num1_är_ett_tal and num2_är_ett_tal:
#     print(f'Summan av {num1} + {num2} är {int(num1)+int(num2)}!')

# elif (not num1_är_ett_tal) and (not num2_är_ett_tal):
#     print(f'Både {num1} och {num2} är inte tal')

# elif num1_är_ett_tal:
#     print(f'Andra inputen {num2} är inte ett tal!')

# else:
#     print(f'Första inputen {num1} är inte ett tal!!')