#-*- coding: utf-8 -*-
jedi = {}

while True:
        j = raw_input("Vpišite jed: ")
        cena = float(raw_input("Vpišite še ceno jedi: "))
        jedi[j] = cena
        if raw_input("Želite na jedilnik dodati novo jed?(da/ne) ").lower() == "ne":
            break

print("Na jedilnik ste dodali: ")
for jed in jedi:
    print (jed, jedi [jed])

with open("menu.txt", "w+") as menu_file:
    menu_file.write ("Danes strežemo: \n")
    for j in jedi:
        menu_file.write("%s, %s EUR\n" % (j, jedi[j]))

