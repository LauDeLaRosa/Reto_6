# Poco A Poco Entendiendo Esto De Programar
## Ejercicio #1
Dado la figura de la imagen, desarrolle una función matemática para calcular el volumen y el área superficial. Para este ejercicio se usó el archivo [funcionesja.py](/funcionesja.py) para importar ciertas funciones.

![image](https://user-images.githubusercontent.com/124603892/227018204-1eba2452-b7da-476d-b668-dc653c3ea9e3.png)

```python
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
```

## Ejercicio #2
Dado la figura de la imagen, desarrolle una función matemática para calcular el área y el perimetro. Para este ejercicio se usó el archivo [funcionesja.py](/funcionesja.py) para importar ciertas funciones.

![image](https://user-images.githubusercontent.com/124603892/227020418-64eb4eaf-7965-4648-a463-acf87b8eb118.png)
```python
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
 ```

## Ejercicio #3
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```python
def calcularKilosCarneAves (N:int, M:int, K:int)->int:
    cantidadCarneAves= (N*6) + (M*7) + (K*1)
    return cantidadCarneAves
if __name__=="__main__":
    N=int(input("Ingrese la cantidad de gallinas:"))
    M=int(input("Ingrese la cantidad de gallos:"))
    K=int(input("Ingrese la cantidad de pollitos:"))
    kilosCarne=calcularKilosCarneAves(N,M,K)
    print("La cantidad de carne de aves es de " + str(kilosCarne) + " kilos")
```

## Ejercicio #4
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
```python
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
```

## Ejercicio #5
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
```python
def calcularValorPrestamo (c:float, i:float, n:int)->float:
    valorPrestamo= c*((1+i)**n)
    return valorPrestamo
if __name__=="__main__":
    c=float(input("Ingrese la cantidad del préstamo:"))
    i=float(input("Ingrese el porcentaje de interés:"))
    n=float(input("Ingrese la cantidad de meses:"))
    valor=calcularValorPrestamo(c,i,n)
    print("El valor del préstamo es de " + str(valor))
```

## Ejercicio #6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```python
def calcularContagiadosCovid (D:int, C:int)->int:
    contagiadosCovid= (2**D)*(C)
    return contagiadosCovid
if __name__=="__main__":
    C=int(input("Ingrese la cantidad de contagiados actuales:"))
    D=int(input("Ingrese la cantidad de días transcurridos:"))
    contagiados=calcularContagiadosCovid(D,C)
    print ("La cantidad de contagiados de Covid-19 en el país de Nuncalandia al transcurrir " + str(C) + " días " + "es de " + str(contagiados) )
```

## Ejercicio #7
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

 + El promedio
 + La mediana
 + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
 + Ordenar los números de forma ascendente
 + Ordenar los números de forma descendente
 + La potencia del mayor número elevado al menor número
 + La raíz cúbica del menor número
Para este ejercicio se usó el archivo [funciones7.py](/funciones7.py) para importar ciertas funciones.
```python
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
    
```

## Ejercicio #8
Archivo [funciones7.py](/funciones7.py)

## Ejercicio #9
Pip en python es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python y descargarlos a nuestra computadora con la finalidad de integrarlos a nuestros desarrollos realizado en python.

## Ejercicio #10
Algunos módulos populares para python que se puedan instalar como pip son:

 + Matplotlib
 + Seaborn
 + Bokeh
 + NumPy
 + SciPy
 + Pandas
 + Numba
 + Scikit-Learn
 + TensorFlow
 + Pillow
 
Para instalar cualquier de estos módulos se debe escribir lo siguiente:
```python
pip install Matplotlib #En lugar de Matplolib escribir el módulo que se quiera instalar
```












