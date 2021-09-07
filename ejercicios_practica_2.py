# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open('stock.csv', 'r')
    stock = list(csv.DictReader(csvfile))
    cantidad_tornillos = 0
    cantidad_arandelas = 0
    cantidad_tuercas = 0
      

    for i in range(len(stock)):
        producto = stock[i]
        for k,v in producto.items():
            if k == "arandelas":
                cantidad_arandelas += int(v)
            elif k == "tornillos":
                 cantidad_tornillos += int(v)
            else:
                cantidad_tuercas += int(v)

    print("La cantidad de arandelas es de", cantidad_arandelas,"\n","la cantidad de tornillos es de", cantidad_tornillos, "\n", "la cantidad de tuercas es de", cantidad_tuercas,)        

           

    csvfile.close()         

import csv

def ej4():
    print('Ejercicios con archivos CSV 2º')
    csvfile = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
        
    csvfile = open('propiedades.csv','r')
    propiedades = list(csv.DictReader(csvfile))
    ambientes_0 = 0
    ambientes_2 = 0
    ambientes_3 = 0
    sin_informacion = 0
    
    for i in range(len(propiedades)):
        depto = propiedades[i]
        for k,v in depto.items():
            try:
                ambientes = int(v) 
                if ambientes == 2:
                    ambientes_2 += int(v)
                elif ambientes == 3:
                    ambientes_3 += int(v)
                elif ambientes == '':      
                   sin_informacion += int(v)        
                else:
                    ambientes_0+= int(v)
            except:
             print("Existen departamentos sin informacion")
    print("Cantidad de departamentos de dos ambientes", ambientes_2)
    print("Cantidad de departamentos de tres ambientes", ambientes_3)   
    print("Departamentos sin datos", sin_informacion)
    print("Departamentos con error datos", ambientes_0)    
            
    csvfile.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
