__author__="juan camilo parra"
__license__="GPL"
__version__="1.0.0"
__Email__="juan.parrasan@campusucc.edu.co"

import Constantes
from Tipo import Tipo
class Producto:

#----------------------------------------------------------------
# Constantes
# ----------------------------------------------------------------

    #IVA_PAPELERIA = 0.16
    IVA_SUPERMERCADO = 0.04
    #IVA_FARMACIA = 0.12

#----------------------------------------------------------------
# Constructor
# ----------------------------------------------------------------

    def __init__(self, nombre, tipo, valorUnitario:float, cantidad:int, cantidadMinima:int, subsidiado: bool, calidad):
        
#----------------------------------------------------------------
# Atributos
#----------------------------------------------------------------
        self.__nombre=nombre
        self.__tipo=tipo
        self.__valorUnitario = valorUnitario
        self.__subsidiado = subsidiado
        self.__calidad = calidad
        self.__cantidadBodega = cantidad
        self.__cantidadMinima = cantidadMinima
        self.__cantidadUnidadesVendidas = 0

#----------------------------------------------------------------
# self.subsidiado = True 
# self.subsidiado = False
#----------------------------------------------------------------

    def CalcularPrecioSupermercador(self):
        self.__valorUnitario += self.__valorUnitario + (self.__valorUnitario * self.IVA_SUPERMERCADO) 

#----------------------------------------------------------------
# Metodos
#----------------------------------------------------------------

#----------------------------------------------------------------
# Hacer estos metodos
# DarNombre
# DarTipo
# DarValorUnitario
# DarCantidadBodega
# DarCantidadMinima
# DarCantidadUnidadesVendidas
#----------------------------------------------------------------

    __method__ = "DarNombre"
    __parameter__ = "Ninguno"
    __returns__ = "Nombre del producto"
    __Description__ = "metodo que retorna el nombre del producto"
    def DarNombre(self):
        return self.__nombre
    
    __method__ = "DarTIpo"
    __parameter__ = "Ninguno"
    __returns__ = "Tipo del producto"
    __Description__ = "Retorna el tipo del producto"
    def DarTIpo(self):
        return self.__tipo
    
    __method__ = "DarValorUnitario"
    __parameter__ = "Ninguno"
    __returns__ = "Valor Unitario"
    __Description__ = "Retorna el Valor Unitario"
    def DarValorUnitario(self):
        return self.__valorUnitario
    
    __method__ = "DarCantidadBodega"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad Bodega"
    __Description__ = "Retorna la cantidad en bodega"
    def DarCantidadBodega(self):
        return self.__cantidadBodega
    
    __method__ = "DarCantidadMinima"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad Minima"
    __Description__ = "Retorna la cantidad minima en bodega"
    def DarCantidadMinima(self):
        return self.__cantidadMinima
    
    __method__ = "DarCantidadUnidadesVendidas"
    __parameter__ = "Ninguno"
    __returns__ = "CantidadUnidadesVendidas"
    __Description__ = "Retorna la cantidad de unidades vendidas"
    def DarCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
   
    __method__ = "DarPublicidad"
    __parameter__ = "Ninguno"
    __returns__ = "Mesnaje publicitario de n producto"
    __Description__ = "Metodo que brinda publicidad de un producto"
    def DarPublicidad(self):
        # Metodo facil ------------------------------------------------------------------
        # return 'compre el producto ' + self.__nombre +'por solo $'+self.__valorUnitario
        # Metodo facil ------------------------------------------------------------------ 
        # Metodo Pro --------------------------------------------------------------------
        return f'compre el producto {self.DarNombre} porsolo $ {self.DarValorUnitario}' 
        # Metodo Pro ---------------------------------------------------------------------
    
    __method__ = "EsIgual"
    __parameter__ = "Producto"
    __returns__ = "True o False segun el resultado"
    __Description__ = "Metodo que permite comparar el producto con otro ingresado por el usuario"
    def EsIgual(self,  producto):
        return self.DarNombre() is producto