dias = int(input("Quantos dias alugados?"))
km = float(input("Quantos Km rodados?"))
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
pagar = (dias * 60) + (km * 0.15)
print(f"O total a pagar e de R${pagar:.2f}")