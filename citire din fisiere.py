angajati_file=open("angajati.txt",  "r")  # r= citire w= scriere , r+ ambele

print(angajati_file.readable()) # verificare daca se poate citi
#print(angajati_file.read()) # afisare tot ce e in fisier
#print(angajati_file.readline())
#print(angajati_file.readline()) # printeaza pe rand linii
#print(angajati_file.readlines()[1]) # pune intr-o lista pe rand fiecare
for angajat in angajati_file.readlines():
    print(angajat) # pune intr-o lista pe rand fiecare

angajati_file.close()  # mereu trebuie inchis