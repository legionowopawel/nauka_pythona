password = "chk"

print ("haslo ma nastepujaca ilosc znakow  = " + str(len(password)))
dlugosc = len(password) -2
srodek = "*" * len(password)
print(password[0] + srodek + password[-1])
