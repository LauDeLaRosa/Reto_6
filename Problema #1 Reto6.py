import funcionesja
def calcularAreaFigura (radio1:float, radio2:float, altura:float) -> float:
    AreaFigura= funcionesja.calcularAreaEsfera(radio1) + funcionesja.calcularAreaCono(radio2, altura)
    return AreaFigura 
def calcularVolumenFigura (radio1:float, radio2:float, altura:float) -> float:
 VolumenFigura= funcionesja.calcularVolumenCono(radio2, altura) + funcionesja.calcularVolumenEsfera(radio1)
 return VolumenFigura
if __name__ == "__main__":
   radio1 = float(input("Ingrese radio de la esfera:"))
   radio2= float(input("Ingrese radio del cono:"))
   altura= float(input("Ingrese altura del cono:"))
   area = calcularAreaFigura(radio1, radio2, altura)
   volumen= calcularVolumenFigura(radio1, radio2, altura)
print("El area de la figura es " + str(area))
print("El volumen de la figura es " + str(volumen))




