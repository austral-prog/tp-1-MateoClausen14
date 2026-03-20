def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    print("Horas completas")
    print(3665//60//60)
    print("Minutos completos restantes")
    print((3665//60//60)%60)
    print("Segundos restantes")
    print(3665%60)
