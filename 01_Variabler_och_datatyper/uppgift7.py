# Här är ett exempel på hur lösningen på Uppgift 7 kan se ut
start_value = input("Skriv in the ursprungliga värdet: ")
current_value = input("Skriv in nuvarande värdet: ")

precision = input("Skriv in önskad precision! 1,2 eller 3\n1. Heltal\n2. Tiondelar\n3. Hundradelar\n>>>")

percent = (int(start_value)-int(current_value))/int(start_value)

if precision == "3":
    print(f"{percent:.2%}")
elif precision == "2":
    print(f"{percent:.1%}")
else:
    print(f"{percent:.0%}")