
class Electrodomestico:
    
    def __init__(self, precioBase = 100, color = "blanco", consumoEnergetico = "F", peso = 5):
        
        self.__precioBase = precioBase

        self.__comprobarColor(color) 

        self.__comprobarConsumoEnergetico(consumoEnergetico)

        self.__peso = peso


    def __comprobarColor(self, color): # aseguramos que el objeto tiene el color adecuado
        
        a = color.lower()
        if  a == "blanco" or a == "negro" or a == "rojo" or a == "azul" or a == "gris":
                self.__color = a
        else:
            color = input("El color no es valido, escriba un color entre blanco, negro, rojo, azul o gris : ")
            self.__comprobarColor(color)
    
    def __comprobarConsumoEnergetico(self, consumoEnergetico):  #aseguramos que tiene el consumo electrico adecuado
        
        consumoEnergetico = consumoEnergetico.upper()
        if  consumoEnergetico == "A" or consumoEnergetico == "B" or consumoEnergetico == "C" or consumoEnergetico == "D" or consumoEnergetico == "E" or consumoEnergetico == "F":
                self.__consumoEnergetico = consumoEnergetico
        else:
            self.__consumoEnergetico = "F"


    def getPrecioBase (self):
        return self.__precioBase

    def getcolor (self):
        return self.__color 

    def getconsumoEnergetico (self):
        return self.__consumoEnergetico

    def getpeso (self):
        return self.__peso

    def setColor(self, color):
        self.__color = color

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



