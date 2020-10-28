for letter in "casa":        #  ia fiecare element de dupa in
    print(letter)
friends =["Maris","Ioana","Carla"]
for friend in friends:
    print(friend)
print("\n")
for i in range(2, 7):   # range i>=2 i<3
    print(i)
print("\n")
for i in range(len(friends)): # lungime lista
    print(friends[i])
print("\n")
for i in range(5):
    if i==0:
        print("primul")

n= int(input("n="))
for i in range(n):   # range i<n
    print(i)
print("\n")

# Functie exponetiala
def exponent (a , b):
    exp=1
    for i in range(b):
        exp=exp*a
    return exp

b= input()
e=input()
print(b+ "^" + e + "=" + str(exponent(int(b),int(e))))

