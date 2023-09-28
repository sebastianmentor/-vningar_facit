ordet = input("Ange ett ord: ").lower()
if ordet == ordet[::-1]:
    print("Ordet är ett palindrom.")
else:
    print("Ordet är inte ett palindrom.")
