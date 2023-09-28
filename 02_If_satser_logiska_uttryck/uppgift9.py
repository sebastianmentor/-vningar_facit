tal1 = float(input("Ange det första talet: "))
tal2 = float(input("Ange det andra talet: "))
tal3 = float(input("Ange det tredje talet: "))

if tal1 > tal2 and tal1 > tal3:
    print("Det första talet är störst.")
elif tal2 > tal1 and tal2 > tal3:
    print("Det andra talet är störst.")
else:
    print("Det tredje talet är störst.")
