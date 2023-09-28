pris = float(input("Ange varans pris: "))
if pris > 1000:
    rabatt = 0.1 * pris
    pris -= rabatt
print(f"Totalpris efter eventuell rabatt: {pris} kr.")