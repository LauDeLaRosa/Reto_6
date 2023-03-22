def calcularContagiadosCovid (D:int, C:int)->int:
    contagiadosCovid= (2**D)*(C)
    return contagiadosCovid
if __name__=="__main__":
    C=int(input("Ingrese la cantidad de contagiados actuales:"))
    D=int(input("Ingrese la cantidad de días transcurridos:"))
    contagiados=calcularContagiadosCovid(D,C)
    print ("La cantidad de contagiados de Covid-19 en el país de Nuncalandia al transcurrir " + str(C) + " días " + "es de " + str(contagiados) )