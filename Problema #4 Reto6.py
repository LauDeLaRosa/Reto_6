import math
def calcularVueltas (P:int, M:int, H:int, B:int)-> int:
    Vueltas=B-((P*300)+(M*3300)+(H*350))
    return Vueltas
if __name__=="__main__":
    P=int(input("Ingrese la cantidad de panes:"))
    M= int(input("Ingrese la cantidad de bolsas de leche:"))
    H=int(input("Ingrese la cantidad de huevos:"))
    B=int(input("Ingrese la cantidad del billete en pesos:"))
    vueltas= calcularVueltas(P,M,H,B)
    print("Las vueltas son "+ str(vueltas) + " pesos")
