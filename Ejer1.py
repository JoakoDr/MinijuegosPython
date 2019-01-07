#Created by Joaquin Díaz

import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)
dado3=random.randint(1,6)
dado4=random.randint(1,6)
print("Carmen ha sacado "+str(dado1)+" y "+str(dado2))
print("David ha sacado "+str(dado3)+" y "+str(dado4))
suma1 = dado1 + dado2
suma2 = dado3 + dado4
if suma1 > suma2:
        print("Carmen ha ganado")

elif suma2>suma1:
    print("David ha ganado")

elif suma1 == suma2 :
    print("Han empatado")



