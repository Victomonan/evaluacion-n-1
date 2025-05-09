import os
import random

x = 0
y = 0

os.system("clear")

campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]

ip_ranges = {
    "zona core": (1, 50),
    "campus uno": (51, 100),
    "campus matriz": (101, 150),
    "sector outsourcing": (151, 200),
}

print("¿Qué quiere hacer?")
print("1. Ver los dispositivos. \n2. Ver los campus. \n3. Añadir dispositivo. \n4. Añadir campus. \n5. Borrar dispositivo. \n6. Borrar campus")


while True:
    try:
        selector = int(input("Elegir una opción: "))
        if selector < 1 or selector > 6:
            raise ValueError("Opción no válida.")
        break
    except ValueError as e:
        print(f"Error: {e}. Intenta nuevamente.")

if selector == 1:
    os.system("clear")
    print("Elige un campus:")
    for i, item in enumerate(campus, start=1):
        print(f"{i}. {item}")

    selector = input("\nElija una opción: ")
    x = int(selector) - 1

    if x >= 0:
        os.system("clear")
        with open(campus[int(x)] + ".txt", "r") as file:
            for item in file:
                item = item.strip()
                print(item)

elif selector == 2:
    os.system("clear")
    print("Lista de campus:")
    for i, item in enumerate(campus, start=1):
        print(f"{i}. {item}")

elif selector == 3:
    os.system("clear")
    print("¿Dónde agregar el nuevo dispositivo?")
    for i, item in enumerate(campus, start=1):
        print(f"{i}. {item}")

    selector = input("\nElija una opción: ")
    x = int(selector) - 1

    if x >= 0:
        os.system("clear")
        with open(campus[int(x)] + ".txt", "a") as file:
            print("Elija un dispositivo: \n \n1. Router. \n2. Switch. \n3. Switch multicapa. \n")
            while True:
                try:
                    variable1 = int(input("Elija su opción: "))
                    if variable1 < 1 or variable1 > 3:
                        raise ValueError("Opción no válida.")
                    break
                except ValueError as e:
                    print(f"Error: {e}. Intenta nuevamente.")

            os.system("clear")
            print("Agregue el nombre de su dispositivo")
            variable2 = input("Agregue su nombre: ")

            while True:
                print("¿Confirma este nombre? \n \n1. Sí \n2. No \n")
                variable3 = input("Introduzca su respuesta: ")
                if variable3 == "1":
                    print("Terminado")
                    break

            print("Elija una jerarquía: \n \n1. Nucleo, \n2. Acceso. \n3. Distribución. \n")
            while True:
                try:
                    variable3 = int(input("Elija una opción: "))
                    if variable3 < 1 or variable3 > 3:
                        raise ValueError("Opción no válida.")
                    break
                except ValueError as e:
                    print(f"Error: {e}. Intenta nuevamente.")

            
            campus_name = campus[x]  
            ip_range_start, ip_range_end = ip_ranges[campus_name] 

            while True:
                ip = input(f"Ingrese la IP del dispositivo (ej: 192.168.20.10): ")
                partes = ip.strip().split(".")

                if len(partes) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in partes):
                    ultimo_octeto = int(partes[3])
                    if ip_range_start <= ultimo_octeto <= ip_range_end:
                        break
                else:
                        print(f"El último octeto ({ultimo_octeto}) no está permitido para {campus_name}. Debe estar entre {ip_range_start} y {ip_range_end}.")
            else:
                print("IP no válida. Usa el formato correcto y valores entre 0-255.")


            file.write("\n---------------------------------\n")
            servicios = []
            vlans = [] 

            if variable1 == 1:
                print("Elija un servicio de red para el router: \n1. Datos \n2. VLAN \n3. Trunking \n4. Salir \n")
                while True:
                    try:
                        variable4 = int(input("Elija una opción: "))
                        if variable4 < 1 or variable4 > 4:
                            raise ValueError("Opción no válida.")
                        if variable4 == 4:
                            break
                        if variable4 == 1:
                            servicios.append("Datos")
                        elif variable4 == 2:
                            servicios.append("VLAN")
                        elif variable4 == 3:
                            servicios.append("Trunking")
                    except ValueError as e:
                        print(f"Error: {e}. Intenta nuevamente.")
                
            elif variable1 == 2:
                print("Elija un servicio de red para el switch: \n1. Datos \n2. VLAN \n3. Trunking \n4. Salir \n")
                while True:
                    try:
                        variable4 = int(input("Elija una opción: "))
                        if variable4 < 1 or variable4 > 4:
                            raise ValueError("Opción no válida.")
                        if variable4 == 4:
                            break
                        if variable4 == 1:
                            servicios.append("Datos")
                        elif variable4 == 2:
                            servicios.append("VLAN")
                        elif variable4 == 3:
                            servicios.append("Trunking")
                    except ValueError as e:
                        print(f"Error: {e}. Intenta nuevamente.")
                file.write("Switch: " + variable2)

            elif variable1 == 3:
                print("Elija un servicio de red para el switch multicapa: \n1. Datos \n2. VLAN \n3. Trunking \n4. Enrutamiento \n5. Salir")
                while True:
                    try:
                        variable4 = int(input("Elija una opción: "))
                        if variable4 < 1 or variable4 > 5:
                            raise ValueError("Opción no válida.")
                        if variable4 == 5:
                            break
                        if variable4 == 1:
                            servicios.append("Datos")
                        elif variable4 == 2:
                            servicios.append("VLAN")
                        elif variable4 == 3:
                            servicios.append("Trunking")
                        elif variable4 == 4:
                            servicios.append("Enrutamiento")
                    except ValueError as e:
                        print(f"Error: {e}. Intenta nuevamente.")
                file.write("Switch multicapa: " + variable2)

            elif selector == 4:
                os.system("clear")
                print("Añadir un nuevo campus")

                nuevo_campus = input("Ingrese el nombre del nuevo campus: ")
                
                if nuevo_campus not in campus:
                    campus.append(nuevo_campus,)
                    ip_ranges[nuevo_campus] = (201, 250)
                    open(nuevo_campus + ".txt", "w").close()
                    print(f"Campus {nuevo_campus} añadido correctamente.")
                
                else:
                    print(f"El campus {nuevo_campus} ya existe.")

            file.write(f"\nIP: {ip}\n")

            if variable3 == 1:
                file.write("\nJerarquía: Nucleo")
            elif variable3 == 2:
                file.write("\nJerarquía: Distribución")
            elif variable3 == 3:
                file.write("\nJerarquía: Acceso")
                
             
            vlan_input = input("¿Ingrese las VLANs configuradas (separadas por comas): ")
            vlans = vlan_input.split(",")
            file.write("\nVLANs: " + ", ".join(vlans))


            file.write("\nServicios: " + str(servicios))
            file.write("\n---------------------------------\n")
