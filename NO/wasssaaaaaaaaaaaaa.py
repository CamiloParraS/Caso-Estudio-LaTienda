import tkinter as tk
from tkinter import messagebox

#------------------------------------
# Constantes
IVA_PAPELERIA = 0.16
IVA_SUPERMERCADO = 0.04
IVA_FARMACIA = 0.12
# Constantes
#------------------------------------

class Producto:
    def __init__(self, nombre, tipo, valor_unitario, cantidad_bodega, cantidad_minima, cantidad_unidades_vendidas):
        self.nombre = nombre
        self.tipo = tipo
        self.valor_unitario = valor_unitario
        self.cantidad_bodega = cantidad_bodega
        self.cantidad_minima = cantidad_minima
        self.cantidad_unidades_vendidas = cantidad_unidades_vendidas
        
    def __repr__(self):
        return f"{self.nombre} ({self.tipo}) - Valor Unitario: {self.valor_unitario}, En Bodega: {self.cantidad_bodega}, Vendidas: {self.cantidad_unidades_vendidas}"

class Tienda:
    def __init__(self, dinero_en_caja):
        self.dinero_en_caja = dinero_en_caja
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __repr__(self):
        return f"Tienda con dinero en caja: {self.dinero_en_caja} y {len(self.productos)} productos."


# Función para mostrar los productos en un MessageBox
def mostrar_productos():
    productos_text = ""
    for producto in tienda.productos:
        productos_text += f"{producto}\n"
    messagebox.showinfo("Productos en Tienda", productos_text)

# Función para realizar un cálculo con el producto de ejemplo
def calcular_operaciones():
    # Ejemplo: cálculo de las unidades de jabón vendidas con IVA
    valor_jabon_vendido = producto3.cantidad_unidades_vendidas * producto3.valor_unitario * (1 + IVA_SUPERMERCADO)
    messagebox.showinfo("Cálculo Jabón", f"Jabón vendido con IVA: {valor_jabon_vendido:.2f}")

# Función para calcular IVA total
def calcular_iva_total():
    iva_total = (producto1.cantidad_unidades_vendidas * IVA_PAPELERIA * producto1.valor_unitario) + \
                (producto2.cantidad_unidades_vendidas * IVA_SUPERMERCADO * producto2.valor_unitario) + \
                (producto3.cantidad_unidades_vendidas * IVA_SUPERMERCADO * producto3.valor_unitario) + \
                (producto4.cantidad_unidades_vendidas * IVA_FARMACIA * producto4.valor_unitario)
    messagebox.showinfo("Total IVA", f"Total del IVA a pagar: {iva_total:.2f}")

# Función para calcular el promedio del valor unitario de los productos
def calcular_promedio_valor():
    promedio_valor_productos = (producto1.valor_unitario + producto2.valor_unitario + producto3.valor_unitario + producto4.valor_unitario) / 4
    messagebox.showinfo("Promedio Valor", f"Promedio valor unitario de los productos: {promedio_valor_productos:.2f}")

# Crear los productos
producto1 = Producto(nombre="libreta", tipo="PAPELERIA", valor_unitario=5500, cantidad_bodega=44, cantidad_minima=15, cantidad_unidades_vendidas=6)
producto2 = Producto(nombre="leche", tipo="SUPERMERCADO", valor_unitario=2100, cantidad_bodega=25, cantidad_minima=10, cantidad_unidades_vendidas=25)
producto3 = Producto(nombre="jabón", tipo="SUPERMERCADO", valor_unitario=4200, cantidad_bodega=36, cantidad_minima=8, cantidad_unidades_vendidas=14)
producto4 = Producto(nombre="aspirina", tipo="FARMACIA", valor_unitario=400, cantidad_bodega=13, cantidad_minima=11, cantidad_unidades_vendidas=32)

# Crear la tienda
tienda = Tienda(dinero_en_caja=0)

# Agregar los productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
tienda.agregar_producto(producto4)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tienda")

# Etiquetas
label_titulo = tk.Label(ventana, text="Sistema de Gestión de Tienda", font=("Arial", 16))
label_titulo.pack(pady=10)

# Botones
boton_mostrar_productos = tk.Button(ventana, text="Mostrar Productos", command=mostrar_productos)
boton_mostrar_productos.pack(pady=5)

boton_calculo_jabon = tk.Button(ventana, text="Calcular Ventas de Jabón", command=calcular_operaciones)
boton_calculo_jabon.pack(pady=5)

boton_iva_total = tk.Button(ventana, text="Calcular IVA Total", command=calcular_iva_total)
boton_iva_total.pack(pady=5)

boton_promedio_valor = tk.Button(ventana, text="Calcular Promedio Valor Productos", command=calcular_promedio_valor)
boton_promedio_valor.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
