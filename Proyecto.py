print("Bienvenido Don Pancho")

frutas = ["manzana", "platano", "melon" ]
limpieza = ["Cloro", "Fabuloso complete del morado", "Jabon"]
golocinas = ["Sabritas", "Dulces", "Charrones"]
otros = ["Pomada", "Juguetes", "Pastillas"]


while True:
    opcion = int(input("Elige una opcion: \n1. Frutas \n2. Limpieza \n3. Frituras y dulces \n4. Otros \n5. Salir \n"))

    if opcion == 1:
        print("Accediste a las frutas")
        for fruta in frutas:
            print(fruta)
        
        agrgarfruta = input("Desea agragar un producto (s/n): ")

        if agrgarfruta.lower() == "s":
            frutanueva = input("Agrega una fruta nueva: ")
            frutas.append(frutanueva)
            for frutanueva in frutas:
                print(frutanueva)
        elif agrgarfruta.lower == "n":
            break

    elif opcion == 2:
        print("Accediste a la seccion de limpieza")
        for limpio in limpieza:
            print(limpio)
        
        agrgarlimpieza = input("Desea agragar un producto (s/n): ")

        if agrgarlimpieza.lower() == "s":
            limpiezanueva = input("Agrega nuevo producto: ")
            limpieza.append(limpiezanueva)
            for limpiezanueva in limpieza:
                print(limpiezanueva)
        elif agrgarlimpieza.lower == "n":
            break

    elif opcion == 3:
        print("Accediste a la seccion de dulces o golocinas")
        for golocina in golocinas:
            print(golocina)
        
        agrgardulce = input("Desea agragar un producto (s/n): ")

        if agrgardulce.lower() == "s":
            dulcenuevo = input("Agrega nuevo producto: ")
            golocinas.append(dulcenuevo)
            for dulcenuevo in golocinas:
                print(dulcenuevo)
        elif agrgardulce.lower == "n":
            break

    elif opcion == 4:
        print("Accediste a la seccion de otros")
        for otro in otros:
            print(otro)
        
        agrgarotro = input("Desea agragar un producto (s/n): ")

        if agrgarotro.lower() == "s":
            otronuevo = input("Agrega nuevo producto: ")
            otros.append(otronuevo)
            for otronuevo in otros:
                print(otronuevo)
        elif agrgarotro.lower == "n":
            break

    elif opcion == 5:
        print("Gracias por visitar Abarrotes Don Pancho. ¡Hasta luego!")
        break
    else:
        print("Opción no válida")

    regresar = input("¿Quieres volver al menú principal? (s/n): ")
    
    if regresar.lower() != "s":
        print("Fin del sistema")
        break