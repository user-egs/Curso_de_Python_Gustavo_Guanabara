largura = float(input("Largura da parede:"))
altura = float(input("Altura da parede:"))
#cada 2m de parede precisa de 1l de tinta
area = largura * altura
litros = area / 2
print(f"Sua parede tem a dimensao de {largura}x{altura} e sua area e de {area:.3f}m²")
print(f"Para printar essa parede, voce vai precisara de {litros:.1f}l de tinta ")