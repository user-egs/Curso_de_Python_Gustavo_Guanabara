#o index comeca com 0
frase = "Aula do Curso de Python"
frase1 = "   Aprenda Python  "

print(frase[4:21:2])
print(frase[:5])
print(frase[17:])
print(frase[5::1])

print(len(frase))
print(frase.count("o"))
print(frase.find("rso"))
print(frase.find("Android"))
print("Curso" in frase)

print(frase.replace("Python","Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

print(frase1.strip())
print(frase1.rstrip())
print(frase1.lstrip())

print(frase.split())
print('-'.join(frase))