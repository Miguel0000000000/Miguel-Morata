def calculadora():
    contador = 1
    while contador==1:
        print("Bienvenido a la calculadora")
        print("Si desea sumar ponga 1, si desea restar ponga 2, si desea multiplicar ponga 3 y si desea dividir ponga 4")
        operacion = int(input())
        print("Ahora pon los numeros que desea clacular")
        primero = int(input())
        segundo = int(input())
        if operacion == 1:
            print(primero + segundo)
        elif operacion == 2:
            print(primero - segundo)
        elif operacion == 3:
            print(primero * segundo)
        elif operacion == 4:
            print(primero/segundo)
        print("Si quieres volver a calcular pon 1 y si quieres salir pon 0")
        contador = int(input())
    print("ADIOS")
calculadora()
