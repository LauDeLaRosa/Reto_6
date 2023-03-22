def calcularKilosCarneAves (N:int, M:int, K:int)->int:
    cantidadCarneAves= (N*6) + (M*7) + (K*1)
    return cantidadCarneAves
if __name__=="__main__":
    N=int(input("Ingrese la cantidad de gallinas:"))
    M=int(input("Ingrese la cantidad de gallos:"))
    K=int(input("Ingrese la cantidad de pollitos:"))
    kilosCarne=calcularKilosCarneAves(N,M,K)
    print("La cantidad de carne de aves es de " + str(kilosCarne) + " kilos")