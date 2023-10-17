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


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    n_d = {"goal_scorers": mp.newMap(42000, 
                                     maptype="PROBING", 
                                     loadfactor=0.5,
                                     cmpfunction=compare_scorers),
           "results": mp.newMap(45000, 
                                maptype="PROBING",
                                loadfactor=0.5,
                                cmpfunction=compare_results),
           "shootouts": mp.newMap(1000, 
                                  maptype="PROBING",
                                  loadfactor=0.5,
                                  cmpfunction=compare_shootouts),
            "MatchResults":mp.newMap(1000, 
                                  maptype="PROBING",
                                  loadfactor=0.5,
                                  cmpfunction=compare_shootouts)}

    
    return n_d

def scorers_lab7(data_structs, maptype, loadfactor):
    data_structs['scorers_lab']=mp.newMap(42000,
                                          maptype=maptype,
                                          loadfactor=loadfactor,
                                          cmpfunction=compare_scorers)
    return data_structs

# Funciones para agregar informacion al modelo

def addData(data_structs, data, llave):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    if llave == "goal_scorers":
        add_score(data_structs[llave], data)
    elif llave == "results":
        add_result(data_structs[llave],data,data_structs["MatchResults"])
    elif llave == "shootouts":
        add_shootout(data_structs[llave], data)
    
    
    
          

def add_result(data_structs, data, data_team):
    addMatchResultByTeam(data_team,data)
    data_date = date.fromisoformat(data["date"])
    anio = data_date.year
    
    if not mp.contains(data_structs, anio):
        elem = lt.newList("ARRAY_LIST", compare_results_list)
        lt.addLast(elem,data)
        mp.put(data_structs, anio, elem)
    else:
        k_v = mp.get(data_structs,anio)
        value = me.getValue(k_v)
        lt.addLast(value, data)
        mp.put(data_structs, anio, value)


def add_shootout(data_structs, data):
    data_date = date.fromisoformat(data["date"])
    anio = data_date.year
    
    if not mp.contains(data_structs, anio):
        elem = lt.newList("ARRAY_LIST", cmpfunction=compare_shootouts_list)
        lt.addLast(elem,data)
        mp.put(data_structs, anio, elem)
    else:
        k_v = mp.get(data_structs,anio)
        value = me.getValue(k_v)
        lt.addLast(value, data)
        mp.put(data_structs, anio, value)

def add_score(data_structs, data):
    data_date = date.fromisoformat(data["date"])
    anio = data_date.year
    
    if not mp.contains(data_structs, anio):
        elem = lt.newList("ARRAY_LIST", cmpfunction=compare_shootouts_list)
        lt.addLast(elem,data)
        mp.put(data_structs, anio, elem)
    else:
        k_v = mp.get(data_structs,anio)
        value = me.getValue(k_v)
        lt.addLast(value, data)
        mp.put(data_structs, anio, value)

def add_scorer(data_structs):
    keys = keys_to_array(data_structs['goal_scorers'])
    for key in lt.iterator(keys):
        k_v = mp.get(data_structs['goal_scorers'],key)
        values = me.getValue(k_v)
        for data in lt.iterator(values):
            scorer= data["scorer"]
            #Revisa que el campo de scorer y minuto no estén vacios
            if scorer and data['minute']:
                if not mp.contains(data_structs['scorers_lab'], scorer):
                    elem = {'scorer':scorer,'goals':1,'avg_time':float(data['minute'])}
                    #El elemento abajo contiene información de las anotaciones del jugador. Por ahora, se probará con el tiempo promedio y el número de goles
                    #elem = {'scorer':scorer,'goals':1,'scores':lt.newList('ARRAY_LIST',compare_scorers),'avg_time':float(data['minute'])}
                    #lt.addLast(elem['scores'],data)
                    mp.put(data_structs['scorers_lab'], scorer, elem)
                else:
                    k_v1 = mp.get(data_structs['scorers_lab'],scorer)
                    scorer_info = me.getValue(k_v1)
                    scorer_info['goals']+=1
                    #lt.addLast(scorer_info['scores'], data)
                    #Usa una fórmula para calcular el nuevo promedio
                    scorer_info['avg_time']= ((scorer_info['avg_time']*(scorer_info['goals']-1))+float(data['minute']))/scorer_info['goals']
                    mp.put(data_structs['scorers_lab'], scorer, scorer_info)

def elements_lab7(scorers_values, scorers_size):
    #Se devolverá esta lista nativa de python para que tabulate pueda procesarla.
    return_scorers=[]
    #Mira si hay más de 6 elementos en la data structure con los jugadores.
    if scorers_size>6:
        for i in range(1,7):
            elem = lt.getElement(scorers_values,i)
            return_scorers.append(elem)
    else:
        for i in range(1,scorers_size+1):
            elem = lt.getElement(scorers_values, i)
            return_scorers.append(elem)
    return return_scorers
def n_elements(data_struct, keys):
    number = 0
    for key in lt.iterator(keys):
        k_v=mp.get(data_struct, key)
        value = me.getValue(k_v)
        number+=lt.size(value)
    return number

def first_last_three_elems(data_struct, keys,n_elements):
    #Devuelve los 3 primeros y 3 últimos elementos en un mapa
    #Data_struct es un mapa
    #Keys es una lista ORDENADA de las llaves de data_struct
    #n_elements es el número total de elementos dentro del mapa. Contando los elementos dentro de una llave.
    #Por ejemplo, si las llaves son años, y se guardan todos los partidos de un año dado en una lista, 
    #n_elements sería el número de partidos

    #Mira si hay más de 6 partidos
    return_list = []
    if n_elements<=6:
        for key in lt.iterator(keys):
            k_v = mp.get(data_struct, key)
            value = me.getValue(k_v)
            for v in lt.iterator(value):
                return_list.append(v)
    else:
        first_key = 1
        first_results = 1
        last_results = 1
        last_key = lt.size(keys)
        
        #Añade 3 primeros resultados
        while first_results<=3:
            i=1
            key = lt.getElement(keys, first_key)
            k_v=mp.get(data_struct, key)
            value = me.getValue(k_v)
            while i<=lt.size(value) and first_results<=3:
                elem = lt.getElement(value, i)
                return_list.append(elem)
                first_results+=1
                i+=1
            first_key+=1
        #Añade últimos 3 resultados
        while last_results<=3:
            key = lt.getElement(keys, last_key)
            k_v=mp.get(data_struct, key)
            value = me.getValue(k_v)
            i=lt.size(value)
            while i>0 and last_results<=3:
                elem = lt.getElement(value, i)
                return_list.append(elem)
                last_results+=1
                i-=1
            last_key-=1
    return return_list

def keys_to_array(data_struct):
    array_list = lt.newList("ARRAY_LIST")
    keys= mp.keySet(data_struct)
    for key in lt.iterator(keys):
        lt.addLast(array_list, key)
    return array_list
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

def compare_scorers(keyname, scorer):
    """Compara dos nombres de jugadores, el primero es una cadena y el segundo es un entry de un map"""
    scorer_entry = me.getKey(scorer)
    if keyname== scorer_entry:
        return 0
    elif keyname>scorer_entry:
        return 1
    else:
        return -1

def scorers_sort_criteria(data1, data2):
    if int(data1['goals'])>int(data2['goals']):
        return True
    elif data1['goals']==data2['goals'] and float(data1['avg_time'])<float(data2['avg_time']):
        return True
    return False

def compare_shootouts(keyname, shootout):
    shootout_entry = me.getKey(shootout)
    if keyname== shootout_entry:
        return 0
    elif keyname>shootout_entry:
        return 1
    else:
        return -1
    
def compare_shootouts_list(data1, data2):
    date1 = date.fromisoformat(data1['date'])
    date2= date.fromisoformat(data2['date'])
    if date1==date2 and data1['home_team']==data2['home_team'] and data1['away_team']== data2['away_team']:
        return 0
    elif date1>date2:
        return 1
    elif date1==date2 and data1['home_team']<data2['home_team']:
        return 1
    elif date1==date2 and data1['home_team']==data2['home_team'] and data1['away_team']<data2['away_team']:
        return 1
    return -1


def shootouts_sort_criteria(data_1, data_2):
    date1 = date.fromisoformat(data_1['date'])
    date2 = date.fromisoformat(data_2['date'])
    if date1>date2:
        return True
    elif date1==date2 and data_1['home_team']<data_2['home_team']:
        return True
    elif date1==date2 and data_1['home_team']==data_2['home_team'] and data_1['away_team']<data_2['away_team']:
        return True
    return False

def compare_results(keyname, year):
    year_entry = me.getKey(year)
    if keyname==year_entry:
        return 0
    elif keyname>year_entry:
        return 1
    else:
        return -1

def compare_results_list(data1, data2):
    date1 = date.fromisoformat(data1['date'])
    date2= date.fromisoformat(data2['date'])
    if date1==date2 and data1['home_team']==data2['home_team'] and data1['away_team']== data2['away_team']:
        return 0
    elif date1>date2:
        return 1
    elif date1==date2 and data1['home_team']<data2['home_team']:
        return 1
    elif date1==date2 and data1['home_team']==data2['home_team'] and data1['away_team']<data2['away_team']:
        return 1
    return -1

def results_sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    

    date1 = date.fromisoformat(data_1['date'])
    date2 = date.fromisoformat(data_2['date'])

    if date1>date2:
        return True
    elif date1==date2 and int(data_1['home_score'])>int(data_2['home_score']):
        return True
    elif date1==date2 and int(data_1['home_score'])+int(data_1['away_score'])>int(data_2['home_score'])+int(data_2['away_score']):
        return True
    return False

def years_new_first_criteria(data1, data2):
    if data1>data2:
        return True
    return False
# Funciones de ordenamiento


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    shootouts= data_structs['shootouts']
    results= data_structs['results']
    scores= data_structs['goal_scorers']

    s_keys = mp.keySet(shootouts)
    r_keys= mp.keySet(results)
    sc_keys = mp.keySet(scores)

    #Ordena los partidos, penalties de cada uno de los años
    for key in lt.iterator(s_keys):
        k_v= mp.get(shootouts, key)
        shootout_list = me.getValue(k_v)
        merg.sort(shootout_list, shootouts_sort_criteria)
        mp.put(shootouts,key, shootout_list)
    
    for key in lt.iterator(r_keys):
        k_v= mp.get(results, key)
        results_list = me.getValue(k_v)
        merg.sort(results_list, results_sort_criteria)
        mp.put(results,key, results_list)
    
    for key in lt.iterator(sc_keys):
        k_v= mp.get(results, key)
        results_list = me.getValue(k_v)
        merg.sort(results_list, results_sort_criteria)
        mp.put(results,key, results_list)

def sort_years_new_first(list):
    merg.sort(list, years_new_first_criteria)
    
    

    
