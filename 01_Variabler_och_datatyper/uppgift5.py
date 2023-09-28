print('Skriv in tre heltal!')

num1 = int(input('Skriv tal 1: '))
num2 = int(input('Skriv tal 2: '))
num3 = int(input('Skriv tal 3: '))


if num1 > num2:
    if num2 > num3:
        print(num1, num2, num3)
    elif num3 > num1:
        print(num3, num1, num2)
    else:
        print(num1, num3, num2)
else:
    if num1 > num3:
        print(num2, num1, num3)
    elif num3 > num2:
        print(num3, num2, num1)
    else:
        print(num2, num3, num1)



if num1 < 0 or num2 < 0 or num3 < 0:
    print('Mindre än noll är också ett tal') 

if num1 == num2 or num2 == num3 or num3 == num1:
    if num1 == num2 == num3:
        print('Alla är lika')
    else:
        print('Du har 2 likadana tal!')
    