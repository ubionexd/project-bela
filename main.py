#created by UbiOne
#Project Bela
#Version 2 - Felolvasás

import playsound

user = "0"
space = "\n\n\n\n\n\n\n\n\n\n\n"

print(space)
print("Betöltés...")

playsound.playsound("loaded.mp3", True)

print(space)
print("Béla betöltve!")
print("Kérlek jelentkezz be!")
print("Felhasználónév:")

playsound.playsound("loginpls.mp3", True)

in_username = input()

if in_username == "UbiOne":
    print(space)
    print("Üdv újra, UbiOne!")
    print("Jelszó:")
    user = "1"
    playsound.playsound("ubionepass.mp3", True)

if in_username == "Musk3t4sl4c1":
    print(space)
    print("Üdv újra, Musk3t4sl4c1!")
    print("Jelszó:")
    user = "2"
    playsound.playsound("musk3t4sl4c1pass.mp3", True)


if user == "1":
    ubione_pass = input()
    if ubione_pass == "UbiOne7240":
        print(space)
        print("Bejelentkezve, mint UbiOne (Admin)")
        playsound.playsound("succes-login.mp3", True)

if user == "2":
    musk3t4sl4c1_pass = input()
    if musk3t4sl4c1_pass == "Ho10La10":
        print(space)
        print("Bejelentkezve, mint Musk3t4sl4c1 (Admin)")
        playsound.playsound("succes-login.mp3", True)


logout = input()

if logout == "Logout":
    if user == "1":
        user = "0"
        print(space)
        print("Kijelentkezés...")
        playsound.playsound("succes-logout.mp3", True)
        print(space)
    if user == "2":
        user = "0"
        print(space)
        print("Kijelentkezés...")
        playsound.playsound("succes-logout.mp3", True)
        print(space)

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