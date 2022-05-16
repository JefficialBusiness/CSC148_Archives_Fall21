def check_fermat(a, b, c, n):
    if ((n > 2) and (a ** n) + (b ** n) == (c ** n)):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")



def inp_values():
    a = int(input("Enter an a value: "))
    b = int(input("Enter a b value: "))
    c = int(input("Enter a c value: "))
    n = int(input("Enter an n value: "))
    check_fermat(a, b, c, n)


inp_values()
