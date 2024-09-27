#Barra de carga 
from tqdm import tqdm

loop = tqdm(total=20000, position=0, leave=False)

for k in range(20000):
    loop.set_description("Cargando...")
    loop.update(1)
loop.close()

#Bienvenida y diccionarios a usar como ejemplo
print("Bienvenido Don Pancho")

frutas = {
    "manzana": 1.5,
    "plátano": 0.8,
    "melón": 3.0
}

limpieza = {
    "Cloro": 30,
    "Fabuloso": 24,
    "Jabon": 15
}

golosinas = {
    "Sabritas": 17, 
    "Dulces": 3, 
    "Charrones": 12
}

otros = {
    "Pomada": 20, 
    "Juguetes": 30, 
    "Pastillas": 26
}

#Aqui empieza la magia 
while True:
    try:
        opcion = int(input("\nElige una opción: \n1. Frutas \n2. Limpieza \n3. Frituras y dulces \n4. Otros \n5. Calcular \n6. Salir \nEn su teclado seleccione un numero del 1 al 6 \n"))

#Seccion de las frutas
        if opcion == 1:
            print("Accediste a las frutas")
            for fruta, precio in frutas.items():
                print(f'{fruta}: ${precio}')
        
        #Agregar un producto     
            agregarfruta = input("\n¿Desea agregar un producto? (s/n): ").lower()

            if agregarfruta == "s" or agregarfruta == "si":
                frutanueva = input("Agrega una fruta nueva: ")
                preciofruta = float(input(f"Ingrese el precio de {frutanueva}: "))
                frutas[frutanueva] = preciofruta
                print(f"{frutanueva} ha sido añadida correctamente con el precio de ${preciofruta}.")
         
         #Modificar un producto 
            modificarfruta = input("\n¿Desea quitar un producto o remplazarlo? (s/n): ").lower()

            if modificarfruta == "s" or modificarfruta == "si":
                frutarara = input("¿Deseas modificar o eliminar una fruta? \nPreciona 'e' para Eliminar y 'm' para Modificar): ").lower()
                
                #Eliminar un producto del diccionario
                if frutarara == "e":
                    for fruta, precio in frutas.items():
                        print(f'{fruta}: ${precio}')
                    elminarfruta = input("Ingresa la fruta a eliminar: ")
                    if elminarfruta in frutas:
                        del frutas[elminarfruta]
                        print(f'La {elminarfruta} ha sido eliminada correctamente')
                    else:
                        print(f'La {elminarfruta} no existe en la lista')

                #Modificar precio de un producto del diccionario
                elif frutarara == "m":
                    for fruta, precio in frutas.items():
                        print(f'{fruta}: ${precio}')
                    reemplasarfruta = input("Ingresa el nombre de la fruta a modificar: ").lower()
                    if reemplasarfruta in frutas:
                        nuevopreciofruta = float(input(f"Ingrese el nuevo precio de {reemplasarfruta}: "))
                        frutas[reemplasarfruta] = nuevopreciofruta
                        print(f"El precio de {reemplasarfruta} ha sido actualizado a ${nuevopreciofruta}.")
                    else:
                        print(f"{reemplasarfruta} no está en el diccionario.")

            elif agregarfruta.lower() == "n" or agregarfruta == "no":
                print("\nRegresando al menú...")    
#---------------------------------------------------------------------------------------------------------------#   
#Lo mismo que en la seccion de las frutas solo que con otras areas 
#Seccion de la limpieza
        elif opcion == 2:
            print("Accediste a la sección de limpieza")
            for limpio, precio in limpieza.items():
                print(f'{limpio}: ${precio}')
            
            agregarlimpieza = input("\n¿Desea agregar un producto? (s/n): ").lower()

            if agregarlimpieza == "s" or agregarlimpieza == "si":
                limpieza_nueva = input("Agrega nuevo producto de limpieza: ")
                precio_limpieza = float(input(f"Ingrese el precio de {limpieza_nueva}: "))
                limpieza[limpieza_nueva] = precio_limpieza
                print(f"{limpieza_nueva} ha sido añadida correctamente.")
            
            modificarlimpieza = input("\n¿Desea quitar un producto o remplazarlo? (s/n): ").lower()

            if modificarlimpieza == "s" or modificarlimpieza == "si":
                limpiezarara = input("¿Deseas modificar o eliminar un elemento? \nPreciona 'e' para Eliminar y 'm' para Modificar: ").lower()
                
                if limpiezarara == "e":
                    for limpio, precio in limpieza.items():
                        print(f'{limpio}: ${precio}')
                    elminarlimpio = input("Ingresa el producto a eliminar: ")
                    if elminarlimpio in limpieza:
                        del limpieza[elminarlimpio]
                        print(f'El {elminarlimpio} ha sido eliminado correctamente')
                    else:
                        print(f'El {elminarlimpio} no existe en la lista')

                elif limpiezarara == "m":
                    for limpio, precio in limpieza.items():
                        print(f'{limpio}: ${precio}')
                    reemplasarlimpio = input("Ingresa el nombre del producto a modificar: ").lower()
                    if reemplasarlimpio in limpieza:
                        nuevopreciolimpio = float(input(f"Ingrese el nuevo precio de {reemplasarlimpio}: "))
                        limpieza[reemplasarlimpio] = nuevopreciolimpio
                        print(f"El precio de {reemplasarlimpio} ha sido actualizado a ${nuevopreciolimpio}.")
                    else:
                        print(f"{reemplasarlimpio} no está en el diccionario.")

            elif agregarlimpieza == "n" or agregarlimpieza == "no":
                print("\nRegresando al menú...")
                
#Seccion de los dulces no se porque le puse golosinas
        elif opcion == 3:
            print("Accediste a la sección de dulces")
            for golosina, precio in golosinas.items():
                print(f'{golosina}: ${precio}')
            
            agregardulce = input("\n¿Desea agregar un producto? (s/n): ").lower()

            if agregardulce == "s" or agregardulce == "si":
                dulcenuevo = input("Agrega nuevo dulce o fritura: ")
                preciodulce = float(input(f"Ingrese el precio de {dulcenuevo}: "))
                golosinas[dulcenuevo] = preciodulce
                print(f"{dulcenuevo} ha sido añadido correctamente.")

            modificardulce = input("\n¿Desea quitar un producto o remplazarlo? (s/n): ").lower()

            if modificardulce == "s" or modificardulce == "si":
                dulcerara = input("\n¿Deseas modificar o eliminar un elemento? \nPreciona 'e' para Eliminar y 'm' para Modificar: ").lower()
                
                if dulcerara == "e":
                    for golosina, precio in golosinas.items():
                        print(f'{golosina}: ${precio}')
                    elminardulce = input("Ingresa el producto a eliminar: ")
                    if elminardulce in golosinas:
                        del golosinas[elminardulce]
                        print(f'El {elminardulce} ha sido eliminado correctamente')
                    else:
                        print(f'El {elminardulce} no existe en la lista')

                elif dulcerara == "m":
                    for golosina, precio in golosinas.items():
                        print(f'{golosina}: ${precio}')
                    reemplasardulce = input("Ingresa el nombre del producto a modificar: ").lower()
                    if reemplasardulce in golosinas:
                        nuevopreciodulce = float(input(f"Ingrese el nuevo precio de {reemplasardulce}: "))
                        golosina[reemplasardulce] = nuevopreciodulce
                        print(f"El precio de {reemplasardulce} ha sido actualizado a ${nuevopreciodulce}.")
                    else:
                        print(f"{reemplasardulce} no está en el diccionario.")

            elif agregardulce == "n" or agregardulce == "no":
                print("\nRegresando al menú...")
            
#Seccion de otros (productos como medicina o juguetes)
        elif opcion == 4:
            print("Accediste a la sección de otros")
            for otro, precio in otros.items():
                print(f'{otro}: ${precio}')
            
            agregarotro = input("\n¿Desea agregar un producto? (s/n): ").lower()

            if agregarotro == "s" or agregarotro == "si":
                otronuevo = input("Agrega algo nuevo: ")
                preciotro = float(input(f"Ingrese el precio de {otronuevo}: "))
                otros[otronuevo] = preciotro
                print(f"{otronuevo} ha sido añadido correctamente.")

            modificarotro = input("\n¿Desea quitar un producto o remplazarlo? (s/n): ").lower()

            if modificarotro == "s" or modificarotro == "si":
                otrorara = input("\n¿Deseas modificar o eliminar un elemento? \n(Eliminar/Modificar): ").lower()
                
                if otrorara == "e":
                    for otro, precio in otros.items():
                        print(f'{otro}: ${precio}')
                    elminarotro = input("Ingresa el producto a eliminar: ")
                    if elminarotro in otros:
                        del otros[elminarotro]
                        print(f'El {elminarotro} ha sido eliminado correctamente')
                    else:
                        print(f'El {elminarotro} no existe en la lista')

                elif otrorara == "m":
                    for otro, precio in otros.items():
                        print(f'{otro}: ${precio}')
                    reemplasarotro = input("Ingresa el nombre del producto a modificar: ").lower()
                    if reemplasarotro in otros:
                        nuevopreciotros = float(input(f"Ingrese el nuevo precio de {reemplasarotro}: "))
                        otros[reemplasarotro] = nuevopreciotros
                        print(f"El precio de {reemplasarotro} ha sido actualizado a ${nuevopreciotros}.")
                    else:
                        print(f"{reemplasarotro} no está en el diccionario.")

            elif agregarotro == "n" or agregarotro == "no":
                print("\nRegresando al menú...")
#Fin de las secciones
#---------------------------------------------------------------------------------------------------------------#

#Una calculadora para calcular ganancias de los productos: Frutas, Limpieza, Dulces, Otros  
        elif opcion == 5:
            
            print("Selecciona la categoría para calcular ganancias:")
            categoria = int(input("1. Frutas\n2. Limpieza\n3. Frituras y dulces\n4. Otros\n"))

        #Esta dividida por categorias para mayor facilidad
            if categoria == 1:
                print("Has seleccionado frutas:")
                for fruta, precio in frutas.items():
                    print(f'{fruta}: ${precio}')

                #Ingresar el producto que esta en el diccionario
                producto = input("Ingresa el nombre del producto que vendiste: ")
                if producto in frutas:

                #Se ingresa el numero de unidades que se vendieron en total ejemplo: se vendieron 50 manzanas
                    cantidad = int(input(f"¿Cuántas unidades de {producto} se vendieron?: "))
                    ganancias = cantidad * frutas[producto]
                    print(f"Las ganancias por {cantidad} unidades de {producto} son: ${ganancias}") #Se da la cantidad que se logro por esas ventas
                else:
                    print("El producto ingresado no está en la lista de frutas.")
#-----------------------------------------------------------------------------------------------#
#Lo mismo pero con las demas secciones xd

            elif categoria == 2:
                print("Has seleccionado limpieza:")
                for limpio, precio in limpieza.items():
                    print(f'{limpio}: ${precio}')
                producto = input("Ingresa el nombre del producto que vendiste: ")
                if producto in limpieza:
                    cantidad = int(input(f"¿Cuántas unidades de {producto} se vendieron?: "))
                    ganancias = cantidad * limpieza[producto]
                    print(f"Las ganancias por {cantidad} unidades de {producto} son: ${ganancias}")
                else:
                    print("El producto ingresado no está en la lista de limpieza.")

            elif categoria == 3:
                print("Has seleccionado frituras y dulces:")
                for golosina, precio in golosinas.items():
                    print(f'{golosina}: ${precio}')
                producto = input("Ingresa el nombre del producto que vendiste: ")
                if producto in golosinas:
                    cantidad = int(input(f"¿Cuántas unidades de {producto} se vendieron?: "))
                    ganancias = cantidad * golosinas[producto]
                    print(f"Las ganancias por {cantidad} unidades de {producto} son: ${ganancias}")
                else:
                    print("El producto ingresado no está en la lista de golosinas.")

            elif categoria == 4:
                print("Has seleccionado otros:")
                for otro, precio in otros.items():
                    print(f'{otro}: ${precio}')
                producto = input("Ingresa el nombre del producto que vendiste: ")
                if producto in otros:
                    cantidad = int(input(f"¿Cuántas unidades de {producto} se vendieron?: "))
                    ganancias = cantidad * otros[producto]
                    print(f"Las ganancias por {cantidad} unidades de {producto} son: ${ganancias}")
                else:
                    print("El producto ingresado no está en la lista de otros.")

            else:
                print("Categoría no válida.")
#Fin de la calculadora 
#---------------------------------------------------------------------------------------------------------#

#Salida del programa con barra de progreso y toda la cosa
        elif opcion == 6:
            loop = tqdm(total=20000, position=0, leave=False)

            for k in range(20000):
                loop.set_description("Cargando...")
                loop.update(1)
            loop.close()
            print("Gracias por visitar Abarrotes Don Pancho. ¡Hasta luego!")
            break
        else:
            print("Opción no válida")

#Para no romper el codigo por si se teclea mal, esto empieza desde el try: 
    except ValueError:
        print("Entrada inválida, por favor ingrese un número.")
    except EOFError:
        print("Algo salió mal.")
    except ZeroDivisionError:
        print("Algo salió mal.")
    except NameError:
        print("Algo salio mal")
