from math import sqrt
cateto_oposto = float(input("Comprimento do cateto oposto:"))
cateto_adjacente = float(input("Comprimento do cateto adjacente:"))

hipotenusa = sqrt((cateto_oposto**2) + (cateto_adjacente**2)) 

print(f"A hipotenusa vai medir {hipotenusa:.2f}")