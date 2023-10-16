﻿"""
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
 """

import config as cf
import model
import time
import csv
import tracemalloc
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        'model':None
    }
    control['model']=model.new_data_structs()
    return control


# Funciones para la carga de datos
def load_data(control, data_size):
    #Indica la ruta de los archivos
    filegoalscorers = load_goal_scorers(data_size)
    fileresults = load_results(data_size)
    fileshootouts = load_shootouts(data_size)

    #Carga los datos y los ordena
    load_data_mask(control['model'], filegoalscorers, fileresults, fileshootouts)
    model.sort(control['model'])

    results = control['model']['results']
    scorers = control['model']['goal_scorers']
    shootouts= control['model']['shootouts']
    scorers_size = mp.size(scorers)
    scorers_values = mp.valueSet(scorers)

    #Se devolverá esta lista nativa de python para que tabulate pueda procesarla.
    return_scorers = []
    return_results= []
    return_shootouts=[]
    #Mira si hay más de 6 elementos en la data structure con los jugadores.
    if scorers_size>6:
        for i in range(1,7):
            elem = lt.getElement(scorers_values,i)
            return_scorers.append(elem)
    else:
        for i in range(1,scorers_size+1):
            elem = lt.getElement(scorers_values, i)
            return_scorers.append(elem)

    #Listas donde se guardarán los años presentes en el archivo de partidos y penalties.
    r_years= lt.newList('ARRAY_LIST')
    s_years = lt.newList('ARRAY_LIST')  

    r_keys= mp.keySet(results)
    for key in lt.iterator(r_keys):
        lt.addLast(r_years, key)
    
    s_keys=mp.keySet(shootouts)
    for key in lt.iterator(s_keys):
        lt.addLast(s_years, key)
    
    #Ordena los años de más reciente a más antiguo
    model.sort_years_new_first(r_years)
    model.sort_years_new_first(s_years)

    #Mira el número de partidos y penalties
    n_results= model.n_elements(results, r_keys)
    n_shootouts=model.n_elements(shootouts, s_keys)
    
    #Retorna 3 primeros y 3 últimos elementos
    return_results=model.first_last_three_elems(results, r_keys, n_results)
    return_shootouts=model.first_last_three_elems(shootouts, s_keys, n_shootouts)



    return return_scorers, return_results, return_shootouts, n_results, n_shootouts
    

def load_data_mask(control, filegoalscorers, fileresults, fileshootouts):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    archivos =lt.newList()
    lt.addLast(archivos,filegoalscorers)
    lt.addLast(archivos,fileresults)
    lt.addLast(archivos,fileshootouts)
    for archivo in lt.iterator(archivos):
        file = cf.data_dir  + archivo
        input_file = csv.DictReader(open(file, encoding='utf-8'))
        if "goalscorers" in archivo:
            llave = "goal_scorers"
        elif "results" in archivo: 
            llave = "results"
        else: 
            llave = "shootouts"
        for dato in input_file:
            
            model.addData(control, dato, llave)
    
        
    
def load_goal_scorers(data_size):
    if data_size==1:
     scores_file =  'goalscorers-utf8-small.csv'
    elif data_size==2:
        scores_file =  'goalscorers-utf8-5pct.csv'
    elif data_size==3:
        scores_file =  'goalscorers-utf8-10pct.csv'
    elif data_size==4:
        scores_file =  'goalscorers-utf8-20pct.csv'
    elif data_size==5:
        scores_file =   'goalscorers-utf8-30pct.csv'
    elif data_size==6:
        scores_file =   'goalscorers-utf8-50pct.csv'
    elif data_size==7:
        scores_file =  'goalscorers-utf8-80pct.csv'
    elif data_size==8:
        scores_file =  'goalscorers-utf8-large.csv'
    return scores_file

def load_shootouts(data_size):
    if data_size==1:
     file =  'shootouts-utf8-small.csv'
    elif data_size==2:
        file =  'shootouts-utf8-5pct.csv'
    elif data_size==3:
        file =  'shootouts-utf8-10pct.csv'
    elif data_size==4:
        file =  'shootouts-utf8-20pct.csv'
    elif data_size==5:
        file =  'shootouts-utf8-30pct.csv'
    elif data_size==6:
        file =  'shootouts-utf8-50pct.csv'
    elif data_size==7:
        file =  'shootouts-utf8-80pct.csv'
    elif data_size==8:
        file =  'shootouts-utf8-large.csv'
    return file

def load_results(data_size):
    
    if data_size==1:
        match_file =  'results-utf8-small.csv'
    elif data_size==2:
        match_file = 'results-utf8-5pct.csv'
    elif data_size==3:
        match_file = 'results-utf8-10pct.csv'
    elif data_size==4:
        match_file =  'results-utf8-20pct.csv'
    elif data_size==5:
        match_file = 'results-utf8-30pct.csv'
    elif data_size==6:
        match_file = 'results-utf8-50pct.csv'
    elif data_size==7:
        match_file = 'results-utf8-80pct.csv'
    elif data_size==8:
        match_file = 'results-utf8-large.csv'
    return match_file


""" def load_goal_scorers(n_d, filename):
    goals_file = cf.data_dir  +filename
    input_file = csv.DictReader(open(goals_file, encoding='utf-8'))
    
    for goals in input_file:
        model.addData(n_d, goals)
    
    return model.dataSize(n_d)
def load_results(n_d, filename):
    resultsfile = cf.data_dir + filename
    input_file = csv.DictReader(open(resultsfile, encoding='utf-8'))
    for results in input_file:
        model.addData(n_d, results)
    return model.dataSize(n_d)


def load_shootouts(n_d, filename):
    shootoutsfile = cf.data_dir  + filename
    input_file = csv.DictReader(open(shootoutsfile, encoding='utf-8'))
    for shootout in input_file:
        model.addData(n_d, shootout)
    return model.dataSize(n_d) """


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
