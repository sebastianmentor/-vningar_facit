ålder = int(input("Ange ålder: "))
if ålder < 13:
    print("Personen är ett barn.")
elif 13 <= ålder < 20:
    print("Personen är en tonåring.")
elif 20<= ålder < 67:
    print("Personen är vuxen")
else:
    print("Personen är pensionär.")
