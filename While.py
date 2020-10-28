i = 1
while i<=10:
    print(i)
    i+=1

# Guessing Game
cuvant_secret = "peste"
cuvant =""
incercare = 0
incercari_limita=3

while cuvant_secret!=cuvant and incercare <incercari_limita  :
    cuvant = input("Ghiceste cuvantul: ")
    incercare += 1
if incercare <= incercari_limita:
    print("Ai castigat")
else:
    print("Ai pierdut")



