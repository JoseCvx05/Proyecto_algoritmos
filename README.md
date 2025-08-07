# Gestor de notas académicas
 Un estudiante nececita llevar un mejor gestion sobre sus totas academicas y el **Objetivo** principal de este proyecto sera mejor y tener una mejor eficiencia sobre las notas. 
 
 El sistema permite al usuario registrar, visualizar, modificar, eliminar, analizar y organizar las notas de los cursos en los que está inscrito, todo desde una interfaz sencilla que se ejecuta en la consola.

 Al cubrir necesidades como la organización de cursos, el seguimiento del progreso académico y la posibilidad de analizar el desempeño en diferentes materias el gestor de notas académicas ayudará a los estudiantes concocer y llevar una mejor gestion sobre su rendimiento y sus notas.
 
## === Requisitos ===

**Funcionales**
    - Registrar nuevo curso
    - Mostrar todos los cursos y notas
    - Calcular promedio general
    - Contar cursos aprobados y reprobados
    - Buscar curso por nombre (búsqueda lineal)
    - Actualizar nota de un curso
    - Eliminar un curso

**No funcionales**

    - Debe usar bucles y condicionales en el codigo
    - El sistema se ejecuta en consola con Python
    - No utiliza librerías externas
    - Debe usar bucles y condicionales en el código

## Pseudocodigo

**Diseño principal del menu**

**Inicio**
    Definir opcion Como Entero
    **MIENTRAS** opcion != 6 HACER
        Imprimir "====== Gestor de notas cadenicas ======"
        Imprimir "1. Registrar nuevo curso"
        Imprimir "2. Mostrar todos los cursos y notas"
        Imprimir "3. Calcular promedio general"
        Imprimir "4. Buscar curso por nombre"
        Imprimir "5. Eliminar un curso"
        Imprimir "6. Salir"
        Imprimir "Seleccione una opción:"
        **Leer** opcion
        **Si** opcion = 1 enntonces
            **registrar_nuevo_curso**
        SiNo 
            Si opcion = 2 enntonces
            **mostrar_cursos_y_notas**
        SiNo 
            Si opcion = 3 enntonces
            **calcular_promedio_general**
        SiNo 
            Si opcion = 4 enntonces
            **buscar_curso_por_nombre**
        SiNo 
            Si opcion = 5 enntonces
            **eliminar_curso**
        SiNo 
            Si opcion = 6 enntonces
            Imprimir "Gracias por usar el Gestor de Notas Académicas
        SiNo
            Imprimir "Opción inválida. Intente de nuevo.
        **Fin_si**
    **FinMientras**
**Fin**