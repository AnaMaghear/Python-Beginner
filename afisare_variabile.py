print("ana are mere")
print(6)
nr = "56"
nume = "Ana"
print(nr)
print(nume)
print( "numarul " + nr + " \" este \nmare" )  # merge doar pt tip string
print( "numele " + nume + " este frumos" )
""" asta e un comentariu """
x, y, z = "mere", "pere", "gutui" # dai valori multiple deodata
print(x)
print(y)
print(z)

x = y = z = 5   # valori egale
print(x)
print(y)
print(z)

x = "Cartea "
y = "este "
z = "frumoasa"
k = x + y + z
print(k)
# STRING
sir = "maine"  # functii pt string folosesti punct
print(sir.upper())
print(sir.isupper())
print(sir.upper().isupper())

print(len(sir)) # lungime sir
print(sir[0])
print (sir[len(sir)-1])
print (sir.index("m"))  # indexul unui element din cuvant

sir2 = "Avem engleza"
print( sir2.replace( "engleza", "franceza"  ) ) # schimbare a doua siruri

# NUMERE
nr = -6
a = 2
b = 3
print(3+4)
print( "buna " + str(nr) + " heiiii" ) # pt a afisa numere impreuna cu string
print(abs(nr))  # abs face modulul
print(pow(a,b))  # a la puterea b
print(max(a,b))  # maxim dintre a si b
print(min(a,b))   # minim dintre a si b
print(round(2.7))   # rotunjeste numarul

from math import *
print(floor(3.7)) # aproximare prin lipsa
print(ceil(3.7)) # aproximare prin adoaus
print(sqrt(4)) # radical

print(2**3) # 2^3

