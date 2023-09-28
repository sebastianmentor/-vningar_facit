age = int(input("Skriv in din ålder: "))

if age >= 18:
    print("Du får ta körkort")
else:
    print("Du får vänta till du är 18 att ta körkort!")

#---------------version 1----------------------
# age = int(input("Skriv in din ålder: "))
# license = input("Har du körkort?(y/n)").lower()

# if license == "y":
#     if age < 18:
#         print("Omöjligt! Man måste vara 18 eller äldre för att ta körkort!")
#     else:
#         print("Gratulerar! Du får köra på vägarna!")
# else:
#     if age >= 18:
#         print("Du får ta körkort")
#     else:
#         print("Du får vänta till du är 18 att ta körkort!")
        
#---------------version 2----------------------

# age = int(input("Skriv in din ålder: "))
# license = input("Har du körkort?(y/n): ").lower()

# if age >= 18:
#     if license == 'y':
#         print("Gratulerar! Du får köra på vägarna!")
#     else:
#         print("Du får ta körkort")

# else:
#     if license == 'y':
#         print("Omöjligt! Man måste vara 18 eller äldre för att ta körkort!")
#     else:
#         print("Du får vänta till du är 18 att ta körkort!")
        
#---------------version 3----------------------

# age = int(input("Skriv in din ålder: "))
# license = input("Har du körkort?(y/n): ").lower()

# if age >= 18 and license == 'y':
#     print("Gratulerar! Du får köra på vägarna!")
# elif age <= 18 and license == 'y':
#     print("Omöjligt! Man måste vara 18 eller äldre för att ta körkort!")
# elif age >= 18:
#     print("Du får ta körkort")
# else:
#     print("Du får vänta till du är 18 att ta körkort!")