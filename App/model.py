"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from datetime import date
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(formato):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    n_d = {"goal_scorers": mp.newMap(formato),
           "results": mp.newMap(formato),
           "shootouts": mp.newMap(formato)}

    
    return n_d



# Funciones para agregar informacion al modelo

def addData(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    data_date = date.fromisoformat(data["date"])
    anio = data_date.year
    
    if not mp.contains(data_structs, anio):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(data_structs, anio, elem)
    else:
        k_v = mp.get(data_structs,anio)
        value = me.getValue(k_v)
        lt.addLast(value, data)   
"""""
def adicionar(name, data):
    
    jugador = data["scorer"]
    
    if not mp.contains(name,jugador):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(name,jugador,elem)
    else:
        k_v =mp.get(name,jugador)
        value = me.getValue(k_v)
        lt.addLast(value,data)
"""                        
        
# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs, nombre):
    # TODO: Realizar el requerimiento 2
    
    lista = lt.newList("ARRAY_LIST") 
     
    if mp.contains(data_structs["goal_scorers"], nombre):
        est = mp.valueSet(data_structs["goal_scorers"])
        for cada in lt.iterator(est):
            if nombre == cada["scorer"]:
                addData(lista,cada)
            return lista
    else:
        return "El jugador no existe"

    
         
    


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def sort_crit_goal(data_1, data_2):
     if float(data_1["date"].replace("-","")) < float(data_2["date"].replace("-","")):
        return True
     elif float(data_1["date"].replace("-","")) == float(data_2["date"].replace("-","")):
        if (data_1["minute"]) < (data_2["minute"]):
            return True
        else:
            return False
     else:
        return False


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
