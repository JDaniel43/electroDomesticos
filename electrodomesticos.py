


class Electrodomestico:
    
    def __init__(self,__precioBase = 100 ,__color = "blanco" ,__consumoEnergetico = "F" , __peso = 5 ):
        assert __color == "blanco" or __color == "negro" or __color == "rojo" or __color == "gris" ,f"color must be white: {__color}" 
        
        self.__precioBase = __precioBase

        self.__color = __color

        self.__consumoEnergeico = __consumoEnergetico

        self.__peso = __peso


    def getPrecioBase (self):
        return self.__precioBase

    def getcolor (self):
        return self.__color 

    def getconsumoEnergetico (self):
        return self.__consumoEnergeico

    def getpeso (self):
        return self.__peso
     

    def precioFinal(self):
        a = self.getconsumoEnergetico()
        b = self.getpeso()
        d = 0 # lo que voy a sumar del consumo electrico
        e = 0 # lo que voy a sumar del peso

        if a == "A":
            d= 100 

        elif a == "B":
            d = 80 

        elif a == "C":
            d = 60 

        elif a == "D":
            d = 50 

        elif a == "E":
            d = 30 

        else:
            d = 10  

        if 19 >= b :
            e = 10
        
        elif b >= 20 and 49 >=b:
            e = 50

        elif b >= 50 and 79 >=b:
            e = 80

        else:
            e = 100

        
        return d + e + self.getPrecioBase()


c= Electrodomestico(100,"blanco","F",5)
print(c.precioFinal())
