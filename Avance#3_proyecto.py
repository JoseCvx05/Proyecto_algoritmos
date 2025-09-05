cursos = [{"curso": "Matemáticas", "nota": 90}, #lista de cursos ya creada
    {"curso": "Historia", "nota": 75}]

def registrar_curso_nota():#ciclo while para que el usuario elija cuando salir 
    while True:
        curso = input("Ingresel nombre del curso a registrar: ")
        nota = float(input("Ingrese la nota del curso (0-100): "))
        if  0 <= nota <= 100: 
            cursos.append({"curso": curso, "nota": nota})
            #las llaves es lo que el programa va a utilizar o cambiar
            print(f"Curso '{curso}' registrado con nota {nota}.\n")
        else:
            print("Error")   
        opcion = input("Desea registrar otro curso (S/N)")
        if opcion == "n": #hasta que la opcion elegida se "n" saldrá del ciclo
            break

def mostrar_curso_nota():
    if cursos:
        print("Notas registradas: ")
        #Nnumerate recorre toda la litas y start hace que en vez de empezar en 0 empieze en 1
        #i es el contador que enumera los cursos y C es lo que contiene los datos del los cursos por cada iteracion
        for i, c in enumerate(cursos, start=1): 
            print(f"{i}. {c['curso']}: {c['nota']}")
    else: 
        print("No hay cursos registrados")

def calcular_promedio():
    if cursos: #verifica que la lista no este vacia 

        #sum para sumar todas las notas
        #len es para saber cuantos elemntos hay en la lista y las dividimos entre ella
        #for c recore la listra y toma los calores de notas en cada curso
        promedio = sum(c["nota"] for c in cursos) / len(cursos)
        print("El promedio general es:", promedio)
    else:
        print("No hay notas para calcular promedio")

def cursos_aprovados_reprovados():
    if cursos:
        # 1 para que sume 1 por cada curso mayores o iguales a 60 al recorrerla con c  
        #luego len toma el total de elementos que hay que cursos y le restra lo valores que son mayores o iguales a 60
        aprovados = sum(1 for c in cursos if c["nota"]>= 60)
        reprovados = len(cursos)- aprovados
        print("La cantidad de cursos aprovados es de: ", aprovados)
        print("La cantidad de cursos reprovados es de: ", reprovados)
    else:
        print("Sin cursos reprovados")

def buscar_curso_nombre(nombre):
    for c in cursos: 
        #c recorre la lista y verifica si es igual a al nombre ingresado por el usuario
        #.lower es para que pase cualquier letra ingresada por el usuario a minuscula
        if c["curso"].lower() == nombre.lower():
            print("Curso ","'", nombre,"'" " encontrado: ", "la nota es de: ", c["nota"], " pts." )
            return
    print("Curso no encontrado")

def actualizar_nota_curso(nombre):
    for c in cursos: #c recorre la lista y verifica si el nombre ingresado por el usuario exista
        #.lower es para que pase cualquier letra ingresada por el usuario a minuscula
        if c["curso"].lower() == nombre.lower():
            #al verificar que exista el curso pide una nueva nota al usuario
            nuevaNota= float(input("Ingrese la nueva nota: "))
            #C recorre la lista y remplaza la nota por la que ha sido ingresada por el usuario
            c["nota"] = nuevaNota
            print("La nota ha sido actualizada", c["curso"], c["nota"])
            return
    print("Curso no encotrado")

"""ciclo while para que al realizar algun cambio o accion el programa no termine
hasta que el usuario elija salir del programa"""

while True:
    print("")
    print("======================================")
    print("===== Gestor de notas academicas =====")
    print("1. Mostrar regristro")
    print("2. Mostrar todos los cursos y notas")
    print("3. calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lieal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (ordenamiento burbuja)")
    print("9. Ordenar cursos por nombre (ordenamiento inserción)")
    print("10. Buscar curso por nombre (búsque binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. salir")
    opcion = int(input("Selecione una opcion: "))
    if opcion == 1: 
        print("== Mostrar registro ==")
        registrar_curso_nota()    
    elif opcion == 2: 
        print("== Mostrar cursos ==")
        mostrar_curso_nota()
    elif opcion == 3: 
        print("== Calcular promedio ==")
        calcular_promedio()
    elif opcion == 4: 
        print("== Buscar curso ==")
        cursos_aprovados_reprovados()
    elif opcion == 5: 
        print("== Buscar curso ==")
        nombre = input("Ingrese el nombre del curso a buscar: ")
        buscar_curso_nombre(nombre)
        break
    elif opcion == 6: 
        print("== Actualizar nota ==")
        nombre = input("Ingrese el nombre de curso a cambiar la nota: ")
        actualizar_nota_curso(nombre)
    elif opcion == 7: 
        print("== Eliminar curso==")
        break
    elif opcion == 8: 
        print("== Ordenar curso por nota ==")
        break
    elif opcion == 9: 
        print("== Ordenar curso por nobre==")
        break
    elif opcion == 10: 
        print("== Burcar curso ==")
        break
    elif opcion == 11: 
        print("== Simular cola de solicitudes  ==")
        break
    elif opcion == 12: 
        print("== Hitoria ==")
        break
    elif opcion == 13: 
        print("Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
        break
    else:
        print("Opción invalida....")
        break