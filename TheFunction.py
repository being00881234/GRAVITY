import tkinter


def gravity(M, m, d):
    G = 6.67321*10**-11
    F = G*M*m /  d**2
    print(F)

J = float(input("The mass of first planet: "))
j = float(input("The mass of second planet: "))
r = float(input("Radius between the planets: "))

gravity(J,j,r)
print("the force on hte planet is","N")