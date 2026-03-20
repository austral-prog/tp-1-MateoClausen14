def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9

    promedio = (nota1 + nota2 + nota3)/3
    nota_máxima = max(nota1, nota2, nota3)
    nota_mínima = min(nota1, nota2, nota3)
    puntos_que_faltan = 10-promedio

    print("promedio")
    print(promedio)
    print("nota máxima")
    print(nota_máxima)
    print("nota mínima")
    print(nota_mínima)
    print("puntos que faltan")
    print(puntos_que_faltan)