





class Electrodomestico:
    
    def __init__(self,precioBase = 100 ,color = "blanco" , consumoEnergetico = "F" , peso = 5 ):
        assert color == "blanco" or color == "negro" or color == "rojo" or color == "gris" ,f"color must be white: {color}" 
    
        self.__precioBase = precioBase

        self.__color = color

        self.consumoEnergetico =  self.__ComprobarConsumoEnergetico(consumoEnergetico)


        self.__peso = peso



    
    def __ComprobarConsumoEnergetico(self, consumoEnergetico):
        if consumoEnergetico == "A" or "F" :
            return consumoEnergetico
        else:
            return "F"  


    def getPrecioBase (self):
        return self.__precioBase

    def getcolor (self):
        return self.__color 

    def getconsumoEnergetico (self):
        return self.consumoEnergetico

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


c= Electrodomestico(100, "blanco", "G", 6)
print(c.getconsumoEnergetico())