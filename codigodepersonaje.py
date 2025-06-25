import  random 
nombres = ["david","ciro", "lauti"];
razas = ["humano", "enano","elfo"];
clases = ["guerrero", "Mago", "Arquero"];
num=random.randint(0,2);
vida = random.randint(50,100);
ataque = random.randint(10,50);
defensa = random.randint(5,30);
print("Su personaje es: ",nombres[num],  "\nraza:", razas[num], "\nclase: ", clases[num])
print("Sus estadisticas son: ")
print("vida: ",vida)
print("ataque: ",ataque)
print("defensa: ",defensa)