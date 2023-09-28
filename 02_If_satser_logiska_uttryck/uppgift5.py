år = int(input("Ange ett år: "))
if (år % 4 == 0 and år % 100 != 0) or (år % 400 == 0):
    print("Det är ett skottår.")
else:
    print("Det är inte ett skottår.")
