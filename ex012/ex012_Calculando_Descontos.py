preco = float(input("Qual e o preco do produto? R$"))
desconto = preco - ((preco * 5) / 100)  
print(f"O produto que custava R${preco:.2f}, na promocao com desconto de 5% vai custar R${desconto:.2f}")