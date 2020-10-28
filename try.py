try:
    raspuns =10/0
    numar = int(input("Introdu un numar:"))  # ca sa nu se opreasca programul intreg
    print(numar)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

