# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 3)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("tonto " + "tu " + "que por que?")
print("nono " + str(5))

# Operaciones mixtas
print("nono " * 5)
print("nono " * (2 ** 3))

my_float = 2.5 * 2
print("nono " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(5 > 4)
print(2 < 4)
print(4 >= 4)
print(4 <= 4)
print(4 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("sisi" > "nono")
print("sisi" < "nono")
print("aaaa" >= "absaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("absaa"))  # Cuenta caracteres
print("sisi" <= "nono")
print("sisi" == "nono")
print("sisi" != "nono")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "sisi" > "nono")
print(3 > 4 or "sisi" > "nono")
print(3 < 4 and "sisi" < "nono")
print(3 < 4 or "sisi" > "nono")
print(3 < 4 or ("sisi" > "nono" and 4 == 4))
print(not (3 > 4))
