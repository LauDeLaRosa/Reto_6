
import statistics
def calcularMedia(x1:float, x2:float, x3:float, x4:float, x5:float) -> float:
 media=float((x1+x2+x3+x4+x5)/5)
 return media

def calcularMediana (x1:float, x2:float, x3:float, x4:float, x5:float) -> float:
    numeros= (x1,x2,x3,x4,x5)
    mediana = statistics.median(numeros)
    return mediana

def calcularPromedioMultiplicativo (x1:float, x2:float, x3:float, x4:float, x5:float) -> float:
 promedioMultiplicativo= float(((x1)* (x2) * (x3) *(x4) *(x5 ))**(1/5))
 return promedioMultiplicativo

def ordenarAscendente (x1:float, x2:float, x3:float, x4:float, x5:float) -> float:
 numeros= (x1,x2,x3,x4,x5)
 ascendente= sorted(numeros)
 return ascendente

def ordenarDescendente (x1:float, x2:float, x3:float, x4:float, x5:float) -> float:
 numeros= (x1,x2,x3,x4,x5)
 descendente= sorted(numeros, reverse=True)
 return descendente

def potenciaMayoralMenor (x1:float, x2:float, x3:float, x4:float, x5:float) -> float:
 mayor=max(x1,x2,x3,x4,x5)
 menor=min(x1,x2,x3,x4,x5)
 potencia= mayor**menor
 return potencia

def raizCubicaMenor (x1:float, x2:float, x3:float, x4:float, x5:float) -> float:
  menor=min(x1,x2,x3,x4,x5)
  raiz=(menor)**(1/3)
  return raiz