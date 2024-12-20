from math import radians,sin,cos,tan
angulo = float(input("Digite o angulo que voce deseja:"))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O angulo de {angulo:.2f} tem o SENO de {seno:.2f}")
print(f"O angulo de {angulo:.2f} tem o COSSENO de {cosseno:.2f}")
print(f"O angulo de {angulo:.2f} tem o TANGENTE DE {tangente:.2f}")