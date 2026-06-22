from math import pi

r = float(input("Enter the value of radius:"))

if r > 0 :
    v = 4/3 * pi * (r**3)
    print("Volume of sphere = ",  format(v, ".2f"))          #format(volume, ".2f")- displays result with 2 decimal places.
else:
    print("Invailid radius")