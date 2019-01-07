#Created by Joaquin Díaz


import random
print("PIEDRA, PAPEL , TIJERA ,LAGARTO, ... , ¡SPOCK!")
sheldon = random.choice(['Piedra', 'Papel', 'Tijera', 'Lagarto', 'Spock'])
leonard = random.choice(['Piedra', 'Papel', 'Tijera', 'Lagarto', 'Spock'])
print("Sheldon ha elegido " + sheldon)
print("Leonard ha elegido " + leonard)
if sheldon == "Piedra" and leonard == "Piedra":
    print("Empate.")
elif sheldon == "Piedra" and leonard == "Papel":
    print("Leonard Gana.")
elif sheldon == "Piedra" and leonard == "Tijera":
    print("Sheldon Gana.")
elif sheldon == "Piedra" and leonard == "Lagarto":
    print("Leonard Gana.")
elif sheldon == "Piedra" and leonard == "Spock":
    print("Sheldon Gana.")
elif sheldon == "Papel" and leonard == "Tijera":
    print("Leonard Gana.")
elif sheldon == "Papel" and leonard == "Papel":
    print("Empate.")
elif sheldon == "Papel" and leonard == "Piedra":
    print("Sheldon Gana.")
elif sheldon == "Papel" and leonard == "Lagarto":
    print("Sheldon Gana.")
elif sheldon == "Papel" and leonard == "Spock":
    print("Leonard Gana.")
elif sheldon == "Tijera" and leonard == "Tijera":
    print("Empate.")
elif sheldon == "Tijera" and leonard == "Papel":
    print("Sheldon gana.")
elif sheldon == "Tijera" and leonard == "Piedra":
    print("Leonard Gana.")
elif sheldon == "Tijera" and leonard == "Lagarto":
    print("Leonard Gana.")
elif sheldon == "Tijera" and leonard == "Spock":
    print("Sheldon Gana.")
elif sheldon == "Lagarto" and leonard == "Piedra":
    print("Sheldon Gana.")
elif sheldon == "Lagarto" and leonard == "Papel":
    print("Leonard Gana.")
elif sheldon == "Lagarto" and leonard == "Tijera":
    print("Sheldon Gana.")
elif sheldon == "Lagarto" and leonard == "Lagarto":
    print("Empate.")
elif sheldon == "Lagarto" and leonard == "Spock":
    print("Leonard Gana.")
elif sheldon == "Spock" and leonard == "Piedra":
    print("Leonard Gana.")
elif sheldon == "Spock" and leonard == "Papel":
    print("Sheldon Gana.")
elif sheldon == "Spock" and leonard == "Tijera":
    print("Leonard Gana.")
elif sheldon == "Spock" and leonard == "Lagarto":
    print("Sheldon Gana.")
elif sheldon == "Spock" and leonard == "Spock":
    print("Empate.")