from math import pi
def calcularAreaEsfera(radio1:float) -> float:
 areaEsfera= ((4*pi)*(radio1**2))
 return areaEsfera


def calcularAreaCono (radio2:float, altura:float)->float:
    generatriz=(((radio2)**2)+((altura)**2))**0.5
    AreaCono=(pi*radio2)*(pi+generatriz)
    return AreaCono


def calcularVolumenEsfera(radio1:float)->float:
   volumenEsfera=((4/3)*(pi)*(radio1**3))
   return volumenEsfera

def calcularVolumenCono(radio2:float, altura:float)->float:
   volumenCono=((1/3)*(pi)*(radio2**2))
   return volumenCono
def calcularAreaCirculo(radio:float)->float:
   areaCirculo=((pi)*(radio**2))
   return areaCirculo

def calcularAreaRectangulo (base:float, altura:float)->float:
   areaRectangulo=base*altura
   return areaRectangulo

def calcularPerimetroRectangulo (base:float, altura:float)->float:
   perimetroRectangulo=(base*2)+(altura*2)
   return perimetroRectangulo

def calcularPerimetroCirculo (radio:float)->float:
   perimetroCirculo=(2*pi*radio)
   return perimetroCirculo


