La tienda

Enunciado

Se desea crear una aplicación que permita manejar el inventario de una tienda, conocer cuánto dinero hay en caja y tener un control de estadísticas de ventas.  

La tienda maneja cuatro productos. De cada uno de ellos se maneja la siguiente información:

- Nombre. No puede haber dos productos con el mismo nombre.
- Tipo (puede ser un producto de papelería, supermercado o droguería).
- Cantidad actual del producto en la tienda (número de unidades disponibles para la venta que hay en bodega.
- Cantidad mínima para abastecimiento (número de productos por debajo del cual se puede hacer un nuevo pedido al proveedor).
- Precio base de venta por unidad.

Para calcular el precio final de cada producto, se deben sumar los impuestos que define la ley (IVA). Dichos impuestos dependen del tipo del producto, de la siguiente manera:

- Papelería: 16%
- Supermercado: 4%
- Droguería: 12%.

Eso quiere decir que si un lápiz tiene un precio base de $10, el precio final será de $11,6 considerando que un lápiz es un producto de papelería, y sobre estos se debe pagar el 16% de impuestos.

El programa debe permitir al usuario:

1. Visualizar la información de los productos.
2. Vender un producto.
3. Abastecer la tienda con un producto.
4. Cambiar un producto.
5. Calcular estadísticas de ventas:

a) El producto más vendido.
b) El producto menos vendido.
c) La cantidad total de dinero obtenido por las ventas de la tienda.
d) La cantidad de dinero promedio obtenido por unidad de producto vendida.
