#Created by Joaquin Díaz


import random
carta1=random.randint(1,10)
carta2=random.randint(1,10)
carta3=random.randint(1,10)
carta4=random.randint(1,10)
carta5=random.randint(1,10)
carta6=random.randint(1,10)
print("Gloria ha sacado "+str(carta1)+" ,"+str(carta2) + " y "+str(carta3))
print("Hector ha sacado "+str(carta4)+" ,"+str(carta5) + " y "+str(carta6))
suma1 = carta1 + carta2 +carta3
suma2 = carta4 + carta5 + carta6
if suma1 > suma2:
    if suma1 < 15 & suma2 < 15:
        print("Gloria ha ganado.")
    else:
        print("No ha ganado nadie.")

elif suma2>suma1:
    if suma1 < 15 & suma2 < 15:
        print("Hector ha ganado.")
    else:
        print("No ha ganado nadie.")
elif suma1 == suma2 :
    if suma1 < 15 & suma2 < 15:
        print("Han empatado.")
    else:
        print("No ha ganado nadie.")
