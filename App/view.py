﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control



def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Ejecutar carga de datos lab 7 (EJECUTAR 1 ANTES)")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    message = """
Ingrese 1 si quiere cargar una muestra pequeña de los datos. 
Ingrese 2 si quiere cargar el 5 porciento de los datos.
Ingrese 3 si quiere cargar el 10 porciento de los datos.
Ingrese 4 si quiere cargar el 20 porciento de los datos
Ingrese 5 si quiere cargar el 30 porciento de los datos.
Ingrese 6 si quiere cargar el 50 porciento de los datos
Ingrese 7 si quiere cargar el 80 porciento de los datos
Ingrese 8 si quiere cargar TODOS los datos."""
    data_size = int(input(message))
    scorers, results, shootouts, n_results, n_shootouts, n_scores = controller.load_data(control, data_size)
    return scorers, results, shootouts, n_results, n_shootouts, n_scores

def print_loaded_data(control):
    scores, results, shootouts, n_results, n_shootouts, n_scores = load_data(control)
    print(f'{"-"*10}\n'
            f'Numero de partidos: {n_results}\n'
            f'Numero de penalties: {n_shootouts}\n'
        f'{"-"*10}\n')
    print(f'Goles encontrados: {n_scores}')
    print(f'{tabulate(scores,headers="keys",tablefmt="grid")}')
    print(f'\nResultados de partidos cargados: {n_results}')
    print(f'{tabulate(results,headers="keys",tablefmt="grid")}')
    print(f'\nResultados de penalties cargados: {n_shootouts}')
    print(f'{tabulate(shootouts,headers="keys",tablefmt="grid")}')

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def print_lab_7(control):
    maptype=input("Ingrese si quiere un mapa PROBING o CHAINING (P/C): ")
    if maptype=="P":
        maptype="PROBING"
    elif maptype=="C":
        maptype="CHAINING"
    load_factor= float(input("Ingrese el factor de carga: "))
    memflag = input("¿Desea que se devuelva registro de la memoria? (T/F): ")
    if "T" in memflag:
        memflag=True
    else:
        memflag = False
    scorers, delta_time, delta_memory = controller.load_data_lab7(control, maptype, load_factor, memflag)
    if scorers:
        print(f'Tiempo de ejecución[ms]: {delta_time:.3f}')
        if delta_memory:
            print(f'Memoria empleada en la ejecución[kB]: {delta_memory:.3f}')
        print(f'Jugadores encontrados:')
        print(f'{tabulate(scorers,headers="keys",tablefmt="grid")}')


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            print_loaded_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs)==10:
            print_lab_7(control)
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
