def calcularValorPrestamo (c:float, i:float, n:int)->float:
    valorPrestamo= c*((1+i)**n)
    return valorPrestamo
if __name__=="__main__":
    c=float(input("Ingrese la cantidad del préstamo:"))
    i=float(input("Ingrese el porcentaje de interés:"))
    n=float(input("Ingrese la cantidad de meses:"))
    valor=calcularValorPrestamo(c,i,n)
    print("El valor del préstamo es de " + str(valor))