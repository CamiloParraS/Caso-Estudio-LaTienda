__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

from Producto import Producto

class Tienda:

#----------------------------------------------------------------
# Constructor
# ----------------------------------------------------------------

    def __init__(self):
    
#----------------------------------------------------------------
# Atributos
#----------------------------------------------------------------
    
        self.__producto1 = None
        self.__producto2 = None
        self.__producto3 = None
        self.__producto4 = None
    
        self.__dineroCaja:float = 0
    
#----------------------------------------------------------------
# Metodos
#----------------------------------------------------------------
    
    __method__='DarProucto1'
    __params__='Ninguno'
    __returns__='Producto1'
    __descriptions__='Este metodo retorna la informacion de producto 1'
    def DarProducto1(self):
        return self.__producto1
        
    __method__='DarProucto2'
    __params__='Ninguno'
    __returns__='Producto2'
    __descriptions__='Este metodo retorna la informacion de producto 2'
    def DarProducto2(self):
        return self.__Producto2
        
    __method__='DarProucto3'
    __params__='Ninguno'
    __returns__='Producto3'
    __descriptions__='Este metodo retorna la informacion de producto 3'
    def DarProducto3(self):
        return self.__Producto3
        
    __method__='DarProucto4'
    __params__='Ninguno'
    __returns__='Producto4'
    __descriptions__='Este metodo retorna la informacion de producto 4'
    def DarProducto4(self):
        return self.__Producto4
                
    __method__='DarDineroCaja'
    __params__='Ninguno'
    __returns__='DineroCaja'
    __descriptions__='Este metodo retorna la informacion de producto 1'
    def darDineroCaja(self):
        return self.__dineroCaja
