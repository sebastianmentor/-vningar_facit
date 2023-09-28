# Här är ett exempel på hur en lösning till uppgift 6 kan se ut
import math

num1 = int(input("Skriv in ett tal: "))
print(f"Kvadraten av {num1} är {num1**2}.")
roten_ur = input(f"Vill du veta vad roten ur av {num1} är? (y/n) :")
if roten_ur == "y":
    print(f"Roten ur {num1} är {math.sqrt(num1):.2f}")