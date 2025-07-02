import  random 
nombres = ["David","Ciro", "Lauti","Tiziano","Emiliano","Axel","Alexis","Hernan","Sofia","Caro","Mailen","Vanesa","Pepe", "Francisco", "Lopez"];
razas = ["Humano", "Enano","Elfo", "Orco","Hobbit","Gnomo","Semielfo","Semiorco","Tiefling","Dragónide" ,"Hada","Goblin","Hombre lagarto", "Aasimar"];
clases = ["Guerrero", "Mago", "Arquero","Clérigo","Chorro","Bárbaro","Bardo","Hechicero","Druida","Monje", "Paladín","ranger","Nigromante","Artificiero", " Cazador de monstruos"];
num=random.randint(0,14);
vida = random.randint(50,100);
ataque = random.randint(10,50);
defensa = random.randint(5,30);
print("Su personaje es: ",nombres[num],  "\nraza:", razas[num], "\nclase: ", clases[num])
print("Sus estadisticas son: ")
print("vida: ",vida)
print("ataque: ",ataque)
print("defensa: ",defensa)
