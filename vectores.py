import math
from pdb import Restart
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

run =1
while run>0:

    print("Vector 1")
    punto1 = input("Ingrese el punto en x: ")
    punto1 = int(punto1)
    punto2 = input("Ingrese el punto en y: ")
    punto2 = int(punto2)
    punto3 = input("Ingrese el punto en z: ")
    punto3 = int(punto3)

    print("Vector 2")
    punto21 = input("Ingrese el punto en x: ")
    punto21 = int(punto21)
    punto22 = input("Ingrese el punto en y: ")
    punto22 = int(punto22)
    punto23 = input("Ingrese el punto en z: ")
    punto23 = int(punto23)

    distancia = math.sqrt((punto21-punto1)*(punto21-punto1)+(punto22-punto2)*(punto22-punto2)+(punto23-punto3)*(punto23-punto3))
    distancia = str(distancia)
    print("Distancia entre ambos vectores: "+distancia)

    norma1 = math.sqrt(punto1*punto1+punto2*punto2+punto3*punto3)
    norma1 = str(norma1)
    print("Norma del primer vector: "+norma1)


    norma2 = math.sqrt(punto21*punto21+punto22*punto22+punto23*punto23)
    norma2 = str(norma2)
    print("Norma del segundo vector: "+norma2)

    direccion1a = punto1/float(norma1)
    direccion1a=str(direccion1a)
    direccion2a = punto2/float(norma1)
    direccion2a=str(direccion2a)
    direccion3a = punto3/float(norma1)
    direccion3a=str(direccion3a)

    direccion1b = punto21/float(norma2)
    direccion1b=str(direccion1b)
    direccion2b = punto22/float(norma2)
    direccion2b=str(direccion2b)
    direccion3b = punto23/float(norma2)
    direccion3b=str(direccion3b)



    print("Dirección vector 1: "+direccion1a+" i, "+direccion2a+" j, "+direccion3a+" k")
    print("Dirección vector 2: "+direccion1b+" i, "+direccion2b+" j, "+direccion3b+" k")


    suma1 = punto1+punto21
    suma2 = punto2+punto22
    suma3 = punto3+punto23

    suma1=str(suma1)
    suma2=str(suma2)
    suma3=str(suma3)


    print("Suma de los vectores: "+suma1+" i, "+suma2+ " j, "+suma3+" k" )


    resta1 = punto1-punto21
    resta2 = punto2-punto22
    resta3 = punto3-punto23

    resta1=str(resta1)
    resta2=str(resta2)
    resta3=str(resta3)

    resta4 = punto21-punto1
    resta5 = punto22-punto2
    resta6 = punto23-punto3

    resta4=str(resta4)
    resta5=str(resta5)
    resta6=str(resta6)

    print("Resta vector 1 - vector 2: "+resta1+" i, "+resta2+ " j, "+resta3+" k" )
    print("Resta vector 2 - vector 1: "+resta4+" i, "+resta5+ " j, "+resta6+" k" )

    producto=((int(punto1)*int(punto21))+(int(punto2)*int(punto22))+(int(punto3)*int(punto23)))
    producto=str(producto)
    print("El escalar resultante del producto entre el vector 1 y 2 es: "+producto)
    
    opcion = input("¿Cuál gráfica desea ver?"+"\n1. Vector 1"+"\n2. Vector 2"+"\n3. Vector resta vector 1 - vector 2"+"\n4. Vector resta vector 2 - vector 1"+"\n5. Vector suma vector 1 + vector 2")
    opcion = int(opcion)

    match opcion:
        case 1:  
            figura = plt.figure()
            plano = figura.add_subplot(projection='3d')
            plt.title("Vector 1")
            a = np.array([int(punto1), int(punto2), int(punto3)])
            plano.scatter(a[0], a[1], a[2], color="red", marker='o')
            plano.plot([0, a[0]], [0, a[1]], [0, a[2]], color="red")
            plano.set_xlim([-30, 30])
            plano.set_ylim([-30, 30])
            plano.set_zlim([-30, 30])
            plano.set_xlabel("x")
            plano.set_ylabel("y")
            plano.set_zlabel("z")
            plt.show()
        case 2:
            figura = plt.figure()
            plano = figura.add_subplot(projection='3d')
            plt.title("Vector 2")
            a = np.array([int(punto21), int(punto22), int(punto23)])
            plano.scatter(a[0], a[1], a[2], color="red", marker='o')
            plano.plot([0, a[0]], [0, a[1]], [0, a[2]], color="red")
            plano.set_xlim([-30, 30])
            plano.set_ylim([-30, 30])
            plano.set_zlim([-30, 30])
            plano.set_xlabel("x")
            plano.set_ylabel("y")
            plano.set_zlabel("z")
            plt.show()
        case 3:
            figura = plt.figure()
            plano = figura.add_subplot(projection='3d')
            plt.title("Vector resta vector 1 - vector 2")
            a = np.array([int(resta1), int(resta2), int(resta3)])
            plano.scatter(a[0], a[1], a[2], color="red", marker='o')
            plano.plot([0, a[0]], [0, a[1]], [0, a[2]], color="red")
            plano.set_xlim([-30, 30])
            plano.set_ylim([-30, 30])
            plano.set_zlim([-30, 30])
            plano.set_xlabel("x")
            plano.set_ylabel("y")
            plano.set_zlabel("z")
            plt.show()
        case 4:
            figura = plt.figure()
            plano = figura.add_subplot(projection='3d')
            plt.title("Vector resta vector 2 - vector 1")
            a = np.array([int(resta4), int(resta5), int(resta6)])
            plano.scatter(a[0], a[1], a[2], color="red", marker='o')
            plano.plot([0, a[0]], [0, a[1]], [0, a[2]], color="red")
            plano.set_xlim([-30, 30])
            plano.set_ylim([-30, 30])
            plano.set_zlim([-30, 30])
            plano.set_xlabel("x")
            plano.set_ylabel("y")
            plano.set_zlabel("z")
            plt.show()
        case 5:
            figura = plt.figure()
            plano = figura.add_subplot(projection='3d')
            plt.title("Suma de los vectores")
            a = np.array([int(suma1), int(suma2), int(suma3)])
            plano.scatter(a[0], a[1], a[2], color="red", marker='o')
            plano.plot([0, a[0]], [0, a[1]], [0, a[2]], color="red")
            plano.set_xlim([-30, 30])
            plano.set_ylim([-30, 30])
            plano.set_zlim([-30, 30])
            plano.set_xlabel("x")
            plano.set_ylabel("y")
            plano.set_zlabel("z")
            plt.show()
    
time.sleep()
