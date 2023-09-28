land = input("Ange ett land: ").lower()

if land == "sverige":
    print("Detta land tillhör Skandinavien")
elif land == "norge":
    print("Detta land tillhör Skandinavien")
elif land == "danmark":
    print("Detta land tillhör Skandinavien")


# Lite klurigare lösning
# if land == "sverige" or land == "norge" or land == "danmark":
#     print("Detta land tillhör Skandinavien")


# Ännu klurigare lösning
# if land in "sverigenorgedanmark":
#     print("Detta land tillhör Skandinavien.")