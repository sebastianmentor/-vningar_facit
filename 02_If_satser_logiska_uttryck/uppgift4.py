temperatur = float(input("Ange temperaturen i Celsius: "))
if temperatur < 0:
    print("Det är jättekallt ute!")
elif 0 <= temperatur <= 10:
    print("Det är rätt så kallt ute!")
elif 11 <= temperatur <= 20:
    print("Vi kanske överlever!")
else:
    print("Nästan så att vi kan tro att det är sommar!")
