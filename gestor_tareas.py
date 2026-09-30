import json
import os

ARCHIVO_DATOS = "tareas.json"

def cargar_tareas():
    """Carga las tareas desde el archivo JSON si existe. Si no, retorna una lista vacía."""
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print("⚠️ Advertencia: El archivo de datos está corrupto. Se iniciará con una lista vacía.")
        return []

def guardar_tareas(tareas):
    """Guarda la lista actual de tareas en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS PROFESIONAL ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    tareas = cargar_tareas()
    
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-5): ").strip()
        
        if opcion == "1":
            if not tareas:
                print("\n📭 No hay tareas registradas.")
            else:
                print("\n--- LISTA DE TAREAS ---")
                for t in tareas:
                    estado = "✅ Completada" | "⏳ Pendiente" if t["completada"] else "⏳ Pendiente"
                    print(f"[{t['id']}] {t['titulo']} - {estado}")
                    
        elif opcion == "2":
            titulo = input("Escribe el título de la nueva tarea: ").strip()
            if titulo:
                nueva_id = tareas[-1]["id"] + 1 if tareas else 1
                nueva_tarea = {
                    "id": nueva_id,
                    "titulo": titulo,
                    "completada": False
                }
                tareas.append(nueva_tarea)
                guardar_tareas(tareas)
                print(f"✨ ¡Tarea '{titulo}' agregada y guardada con éxito!")
            else:
                print("❌ El título no puede estar vacío.")
                
        elif opcion == "3":
           if not tareas:
                print("\n📭 No hay tareas para marcar.")
           else:
                try:
                    id_buscar = int(input("Ingresa el ID de la tarea que completaste: "))
                    encontrada = False
                    for t in tareas:
                        if t["id"] == id_buscar:
                            t["completada"] = True
                            guardar_tareas(tareas)
                            print(f"🎉 ¡Tarea '{t['titulo']}' marcada como completada!")
                            encontrada = True
                            break
                    if not encontrada:
                        print("❌ No se encontró ninguna tarea con ese ID.")
                except ValueError:
                    print("❌ Error: Debes ingresar un número entero válido.")
            
        elif opcion == "4":
           if not tareas:
                print("\n📭 No hay tareas para eliminar.")
           else:
                try:
                    id_buscar = int(input("Ingresa el ID de la tarea que deseas eliminar: "))
                    # Filtramos la lista para conservar solo las tareas cuyo ID sea DIFERENTE al ingresado
                    tareas_filtradas = [t for t in tareas if t["id"] != id_buscar]
                    
                    if len(tareas_filtradas) == len(tareas):
                        print("❌ No se encontró ninguna tarea con ese ID.")
                    else:
                        # Actualizamos la lista original y guardamos en el JSON
                        tareas[:] = tareas_filtradas
                        guardar_tareas(tareas)
                        print("🗑️ Tarea eliminada y cambios guardados con éxito.")
                except ValueError:
                    print("❌ Error: Debes ingresar un número entero válido.")
            
        elif opcion == "5":
            print("\n¡Guardando y saliendo del sistema. Hasta mañana!")
            break
        else:
            print("❌ Opción inválida. Elige un número del 1 al 5.")

if __name__ == "__main__":
    main()