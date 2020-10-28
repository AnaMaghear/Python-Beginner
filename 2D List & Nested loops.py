number_grid= [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:  # afisare fiecare termen din matrice, cu doar primul for afisai randurile
    for col in row:
        print(col)

#translator (schimabre vocale cu un altul)

def translate (propozitie):
    traducere =""
    for letter in propozitie:
        if letter.lower() in "aeiou":  # cautare intr-un sir a unui caracter cu in ; pui .lower ca sa nu mai scrii si cu litera mare
           if letter.isupper():
               traducere= traducere +"G"
           else:
            traducere = traducere +"g"
        else:
            traducere = traducere+letter
    return traducere

print(translate(propozitie=input("Introduceti o propozitie")))



