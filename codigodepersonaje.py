import  random 
nombres = ["david","ciro", "lauti"];
razas = ["humano", "enano","elfo"];
clases = ["guerrero", "Mago", "Arquero"];
num=random.randint(0,2);
vida = random.randint(50,100);
ataque = random.randint(10,50);
defensa = random.randint(5,30);
print("su personaje es: ", nombres[num])
print("su raza es: ", razas[num])
print("su clase es: ", clases[num])
print("de vida tiene: ", vida)
print("de ataque tiene: ", ataque)
print("de defensa tiene: ", defensa)