
def spunebuna():    # Definirea unei functii  cu def nume_functie ():
    print("Hello")      # ce e fix sub nume e luat ca linii din ea, grija cu spatiile


spunebuna()

def say_hi(name, age):
    print("Hello " + name+ ", you re " + str(age))

say_hi("Ana", 35)

def cub (nr):  # Definire functii cu return, nu poti sa printezi cand faci o functie cu return
    a=nr*nr*nr
    return a

print(cub(3))
rezultat= cub(4)
print(rezultat)