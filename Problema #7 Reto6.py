import funciones7

if __name__=="__main__":
    x1=float(input("Ingrese el primer número:"))
    x2=float(input("Ingrese el segundo número:"))
    x3=float(input("Ingrese el tercer número:"))
    x4=float(input("Ingrese el cuarto número:"))
    x5=float(input("Ingrese el quinto número:"))
    media=funciones7.calcularMedia(x1,x2,x3,x4,x5)
    mediana=funciones7.calcularMediana(x1,x2,x3,x4,x5)
    promedioMultiplicativo=funciones7.calcularPromedioMultiplicativo(x1,x2,x3,x4,x5)
    ordenAscendente=funciones7.ordenarAscendente(x1,x2,x3,x4,x5)
    ordenDescendente=funciones7.ordenarDescendente(x1,x2,x3,x4,x5)
    potencia=funciones7.potenciaMayoralMenor(x1,x2,x3,x4,x5)
    raiz=funciones7.raizCubicaMenor(x1,x2,x3,x4,x5)
    print("El promedio es " + str(media))
    print("La mediana es " + str(mediana))
    print("El promedio multiplicativo es " + str(promedioMultiplicativo))
    print("El orden ascendente es " + str(ordenAscendente))
    print("El orden descendente es " + str(ordenDescendente))
    print("La potencia de número mayor elevado al número menor " + str(potencia))
    print("La raiz cúbica del menor número es "+ str(raiz))
    