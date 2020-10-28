is_male = True
is_tall = True
if is_male or is_tall:  # sau = or   si=and
    print("You are a male")
elif is_male and not(is_tall):
    print("blaaa")
# elif= else if not(is tall) negheaza
else:
    print("You are not a male")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num1:
        return num2
    else:
        return num3

print(max_num(7,20,5))

# Calculator mai bun
num1 = float(input("Primul numar: "))
op = input("Operator:")
num2 =float(input("Al doilea numar:"))

if op == "+":
    print("Suma este")
    print(num1+num2)
elif op=="-":
    print("Diferenta este:")
    print(num1 - num2)
elif op=="*":
    print("Produsul este:")
    print(num1 * num2)
elif op == "/" :
    print("Impartirea este: ")
    print(num1 / num2)
else:
    print("Ivalid operator")


