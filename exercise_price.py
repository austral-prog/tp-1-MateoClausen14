def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    precio_base = 100
    monto_impuesto = precio_base*21/100
    monto_subtotal = precio_base+monto_impuesto
    monto_propina = precio_base/10
    monto_final = monto_subtotal+monto_propina
    print(monto_impuesto)
    print(monto_subtotal)
    print(monto_propina)
    print(monto_final)