import funcionesja
def calcularAreaFigura (altura:float, base:float, radio:float)->float:
 areaFigura= ((funcionesja.calcularAreaCirculo(radio))*2)  + funcionesja.calcularAreaRectangulo(base, altura)
 return areaFigura
def calcularPerimetroFigura (altura:float, base:float, radio:float)->float:
 perimetroFigura= ((funcionesja.calcularPerimetroCirculo(radio))*2) + funcionesja.calcularPerimetroRectangulo(base, altura)
 return perimetroFigura
if __name__=="__main__":
 altura=float(input("Ingrese la altura:"))
 base= float(input("Ingrese la base:"))
 radio= float(input("Ingrese el radio:"))
 perimetro= calcularPerimetroFigura(altura, base, radio)
 area= calcularAreaFigura(altura, base, radio)
 print ("El area de la figura es " + str(area))
 print ("El perimetro de la figura es " + str(perimetro))
