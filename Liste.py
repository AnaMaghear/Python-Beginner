friends = ["Bianca", 2, False,"Maria", "Carmen"]  # false cu F mare
print(friends)
print(friends[2])
print(friends[-1])  # negativele incep idexurile de la dreapta la stanga , incepand cu 1
print(friends[2:])  # afiseaza toate elementele de la indexul ala inclusiv
print(friends[1:3]) # afiseaza elementele dintre [1,3) (nu il pune pe ultimul)
friends[1]= 6
print(friends)
print("\n")

# Functii cu Liste

numere_norocoase = [4,8,15,16,23,42,4]
friends = ["Kevin", "Karen", "Jim", "Oscar","Toby"]
friends.extend(numere_norocoase) # Adaugare a unei liste la o lista
print(friends)
friends.append("Creed") # Adauga la fianlul unei liste
print(friends)
friends.insert(1, "kelly")  # Insereaza pe un idex o alta valoare
print(friends)
friends.remove("Toby") # Scoate un element din lista
print(friends)
friends.pop()   #  Scoate ultimul element
print(friends)
friends2= friends.copy() # copiaza lista
friends.clear() # Curata lista de toate elementele
print(friends)
print(numere_norocoase.index(4))  # idexul unui termen
print(numere_norocoase.count(4)) #numara de cate ori apare un element din sir
print("Numarul 4 apare de " + str(numere_norocoase.count(4)) + " ori")
numere_norocoase.sort()  # sortare
print(numere_norocoase)
numere_norocoase.reverse() # inverseaza ordinea
print(numere_norocoase)
print(friends2)

