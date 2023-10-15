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
           "shootouts": mp.newMap(formato),
           "away_teams":mp.newMap(formato),
           "home_teams":mp.newMap(formato), 
           "teams":mp.newMap(formato)}

    
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
def agregar(data_home, data_away, data_juntos, data):

    local = date.fromisoformat(data["home_team"])
    visitante= date.fromisoformat(data["away_team"])
    
    if not mp.contains(data_home,local ):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(data_home,local, elem)
    else:
        k_v = mp.get(data_home,local)
        value = me.getValue(k_v)
        lt.addLast(value, data) 
    if not mp.contains(data_away,visitante ):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(data_away,visitante, elem)
    else:
        k_v = mp.get(data_away,visitante)
        value = me.getValue(k_v)
        lt.addLast(value, data) 
    if not mp.contains(data_juntos,visitante ):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(data_juntos,visitante, elem)
    else:
        k_v = mp.get(data_juntos,visitante)
        value = me.getValue(k_v)
        lt.addLast(value, data)
    if not mp.contains(data_juntos,local ):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(data_juntos,local, elem)
    else:
        k_v = mp.get(data_juntos,local)
        value = me.getValue(k_v)
        lt.addLast(value, data)
     
    
        
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


def req_1(data_structs, condicion,pais):
    """
    Función que soluciona el requerimiento 1
    """
    if condicion == "local":
        estructura=data_structs["home_teams"]
        lista= mp.get(estructura,pais)
        return me.getValue(estructura,lista)
    elif condicion == "visitante":
        estructura=data_structs["away_teams"]
        lista= mp.get(estructura,pais)
        return me.getValue(estructura,lista)
    else:
        estructura= data_structs["teams"]
        lista= mp.get(estructura,pais)
        return me.getValue(estructura,lista)

    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


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


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
