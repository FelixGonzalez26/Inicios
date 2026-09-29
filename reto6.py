def validar_num():
    while True:
        try:
            num = input("Ingrese un número válido: ")
            valor = float(num)
            if valor > 0:
                return valor
            print("❌ Debe ser un número mayor a 0.")
        except ValueError:
            print("❌ No se permiten letras o valores inválidos.")


def mostrar_menu():
    print("\n--- INVENTARIO ---")
    print("1. Insertar Producto")
    print("2. Actualizar Producto")
    print("3. Consultar Producto")
    print("4. Calcular valor total del inventario")
    print("5. Comprar producto")
    print("6. Eliminar producto")
    print("7. Salir")


def Inventario():
    inventario = {}

    while True:
        mostrar_menu()
        opcion = input("\nIngrese una opción (1-7): ").strip()

        # 1. Inserción del producto
        if opcion == "1":
            nombre = input(
                "Ingrese el producto que desea registrar: "
            ).strip().capitalize()
            if nombre in inventario:
                print(
                    f"⚠️ El producto '{nombre}' ya existe. Usa la opción de actualizar."
                )
            else:
                print("Ingrese el precio:")
                precio = validar_num()
                print("Ingrese la cantidad en stock:")
                cantidad = validar_num()

                # Guardamos ambos en un diccionario interno
                inventario[nombre] = {"precio": precio, "cantidad": cantidad}
                print(f"✅ Producto '{nombre}' añadido con éxito.")

        # 2. Actualización
        elif opcion == "2":
            nombre = input(
                "Ingrese el nombre del producto que desea actualizar: "
            ).strip().capitalize()
            if nombre in inventario:
                print(
                    f"Datos actuales de {nombre}: Precio: ${inventario[nombre]['precio']}, Cantidad: {inventario[nombre]['cantidad']}"
                )
                print("Ingrese el nuevo precio:")
                nuevo_precio = validar_num()
                print("Ingrese la nueva cantidad:")
                nueva_cantidad = validar_num()

                inventario[nombre] = {
                    "precio": nuevo_precio,
                    "cantidad": nueva_cantidad,
                }
                print(f"✅ Producto '{nombre}' actualizado correctamente.")
            else:
                print(f"❌ El producto '{nombre}' no existe.")

        # 3. Consultar producto
        elif opcion == "3":
            nombre = input(
                "Ingrese el nombre del producto a consultar: "
            ).strip().capitalize()
            if nombre in inventario:
                datos = inventario[nombre]
                print(
                    f"📦 Producto encontrado: {nombre} -> Precio: ${datos['precio']} | Stock: {datos['cantidad']}"
                )
            else:
                print(f"❌ El producto '{nombre}' no existe.")

        # 4. Precio total del inventario (¡Te dejo este reto para que lo completes o lo mires aquí!)
        elif opcion == "4":
            if not inventario:
                print("⚠️ El inventario está vacío.")
            else:
                total_inventario = 0
                for prod, datos in inventario.items():
                    subtotal = datos["precio"] * datos["cantidad"]
                    total_inventario += subtotal
                print(
                    f"💰 El valor monetario total del inventario es: ${total_inventario:.2f}"
                )
# 5. Vender Producto
        elif opcion == "5":
            nombre = input(
                "Ingrese el nombre del producto que desea comprar: "
            ).strip().capitalize()
            cantidad = validar_num()
            if nombre in inventario:
                datos = inventario[nombre]
                if datos["cantidad"] >= cantidad:
                    subtotal = datos["precio"] * cantidad

                    # ¡Aquí restamos la cantidad del stock actual!
                    inventario[nombre]["cantidad"] -= cantidad

                    print(f"✅ ¡Venta exitosa!")
                    print(f"El costo total de la venta es: ${subtotal:.2f}")
                    print(
                        f"Stock restante de '{nombre}':"
                        f" {inventario[nombre]['cantidad']}"
                    )
                else:
                    print(
                        "❌ No hay suficiente producto en stock. Stock"
                        f" disponible: {datos['cantidad']}"
                    )
            else:
                print("❌ El producto no existe en el inventario.")

        elif opcion=="6":
            nombre= input("Introduzca el nombre del producto que desea eliminar: ").strip().capitalize()
            if nombre in inventario:
                del inventario[nombre]
                print(f"🗑️ producto '{nombre}' eliminado.")
            else:
                print(f"❌ El producto '{nombre}' no existe.")

        
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Elija un número entre 1 y 5.")


# Ejecutar el sistema
Inventario()
                

