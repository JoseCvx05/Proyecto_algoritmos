# Avance #2 proyecto 


**Algoritmno notasEstudiantes**
//Algoritmo principal

Definir promedio como real
//Lama a la función de las notas y nos devuelve el promedio
promedio <- calcularPromedio
//Muestra el promedio
Escribir "El promedio de las notas es: ", promedio
**FinAlgoritmo**

## == Función calcularPromedio() ==
Definir notas, suma como real
Definir CantNotas, i como entero
i <- 1
Escribir "Cuantas notas desea ingresar?"
Leer CantNotas
//Evalua la cantidad de notas y que sea mayores a 0
Si cantNotas <= 0 entonces 
Escribir "Debe ingresar una nota mayor a 0"
Reronar 0
Finsi

Para i hasta cantNotas hacer
nota <- SolicitarNotas
suma <- suma + nota
Finpara

Reroenar suma/CantNotas
# Finfunción

## Función SolicitarNotas(NumNotas)
Definir notas como real
Definir NotaValida como logico
NotaValida <- Falso
Repetir 
Escribir "Ingrese la nota: ", NumNota
Leer notas
//valia el rengo de las notas
Si notas >= 0 Y notas <= 100 entonces 
NotaValida <- Verdadero
sino 
Escribir "Error, tiene que ingresar una nota entre 0 y 100"
Finsi
Hasta notaValidad <- Verdadero
# FinFuncion