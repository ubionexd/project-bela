#created by UbiOne
#Project Bela
#Version 1 - Log in system

user = "0"
logedinas1 = "\n\n\n\n\n\n\n\n\n\n\nBejelentkezve, mint UbiOne!"
logedinas2 = "\n\n\n\n\n\n\n\n\n\n\nBejelentkezve, mint Musk3t4sl4c1!"

print("Béla betöltve!")
print("Kérlek jelentkezz be!")

print("Felhasználónév:")
in_username = input()

if in_username == "UbiOne":
    print("Üdv újra, UbiOne!")
    print("Jelszó:")
    user = "1"

if in_username == "Musk3t4sl4c1":
    print("Üdv újra, Musk3t4sl4c1!")
    print("Jelszó:")
    user = "2"


if user == "1":
    ubione_pass = input()
    if ubione_pass == "UbiOne7240":
        print(logedinas1)

if user == "2":
    musk3t4sl4c1_pass = input()
    if musk3t4sl4c1_pass == "Ho10La10":
        print(logedinas2)


logout = input()

if logout == "Logout":
    if user == "1":
        user = "0"
    if user == "2":
        user = "0"

if user == "0":
    print("Kérlek jelentkezz be!")

print("Felhasználónév:")
in_username = input()

if in_username == "UbiOne":
    print("Üdv újra, UbiOne!")
    print("Jelszó:")
    user = "1"

if in_username == "Musk3t4sl4c1":
    print("Üdv újra, Musk3t4sl4c1!")
    print("Jelszó:")
    user = "2"


if user == "1":
    ubione_pass = input()
    if ubione_pass == "UbiOne7240":
        print("Bejelentkezve, mint UbiOne!")

if user == "2":
    musk3t4sl4c1_pass = input()
    if musk3t4sl4c1_pass == "Ho10La10":
        print("Bejelentkezve, mint Musk3t4sl4c1!")