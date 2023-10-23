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
from DISClib.ADT import orderedmap as mpo
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from datetime import date, timedelta
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
                                     cmpfunction=compare_elements),
           "results": mp.newMap(45000, 
                                maptype="PROBING",
                                loadfactor=0.5,
                                cmpfunction=compare_elements),
           "shootouts": mp.newMap(1000, 
                                  maptype="PROBING",
                                  loadfactor=0.5,
                                  cmpfunction=compare_elements),
            "teams":mp.newMap(1000, 
                                  maptype="PROBING",
                                  loadfactor=0.5,
                                  cmpfunction=compare_elements),
            "goal_scorers_by_year":mp.newMap(42000,
                                        maptype="PROBING", 
                                        loadfactor=0.5,
                                        cmpfunction=compare_elements),
            "jugador_goles": mp.newMap(1000,
                                       maptype="PROBING",
                                       loadfactor= 0.5,
                                       cmpfunction= cmp_req_2_final),
            #Guarda los equipos que participaron en un torneo para un año determinado.
            "teams_tournament_year": mp.newMap(1000,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements),

            #Guarda para un equipo, los partidos que sucedieron en un torneo para un año determinado.
            "team_year_tournament_matches":mp.newMap(1000,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements),
            #Tiene los goles para una fecha específica (incluído año, mes y día)
            'scores_date':mp.newMap(1000,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements),
            'tournaments_by_year':mp.newMap(100,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements),
            'shootouts_date': mp.newMap(1000, 
                                  maptype="PROBING",
                                  loadfactor=0.5,
                                  cmpfunction=compare_elements),
    }

    
    return n_d

def scorers_lab7(data_structs, maptype, loadfactor):
    data_structs['scorers_lab']=mp.newMap(42000,
                                          maptype=maptype,
                                          loadfactor=loadfactor,
                                          cmpfunction=compare_elements)
    return data_structs

# Funciones para agregar informacion al modelo

def addData(data_structs, data, llave):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    data_date = date.fromisoformat(data["date"]).year
    add_element(data_structs[llave],data,data_date)
    if llave=="results":
        addMatchResultsByTeam(data_structs,data)
        add_teams_tournament_year(data_structs, data)
        req6_add_tournament(data_structs['tournaments_by_year'],data)

    if llave=="goal_scorers":
        adicionar_jugador_goles(data_structs, data['scorer'], data)
          

def add_element(data_structs, data):
    #TODO xime 
    data_date = date.fromisoformat(data["date"]).year
    """
    if not mp.contains(data_structs, data_date):
        elem = lt.newList("ARRAY_LIST", cmpfunction=compare_elements)
    addMatchResultsByTeam(data_team,data)
    """
    if not mp.contains(data_structs, data_date):
        elem = lt.newList("ARRAY_LIST", compare_elements)
        lt.addLast(elem,data)
        mp.put(data_structs, data_date, elem)
    else:
        k_v = mp.get(data_structs,data_date)
        value = me.getValue(k_v)
        lt.addLast(value, data)
        mp.put(data_structs, data_date, value)
    
def add_shootout_date(data_structs, data):
    data_date = date.fromisoformat(data["date"])
    if not mp.contains(data_structs, data_date):
        elem = lt.newList("ARRAY_LIST", compare_results_list)
        lt.addLast(elem,data)
        mp.put(data_structs, data_date, elem)
    else:
        k_v = mp.get(data_structs,data_date)
        value = me.getValue(k_v)
        lt.addLast(value, data)
        mp.put(data_structs, data_date, value)

def add_teams_tournament_year(data_structs, data):
    tournament = data['tournament']
    map1 = data_structs['teams_tournament_year']
    year = date.fromisoformat(data["date"]).year
    if not mp.contains(map1, tournament):
        #Este mapa contiene los torneos.
        elem = mp.newMap(1000,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements)
        mp.put(map1, tournament, elem)

    map2=me.getValue(mp.get(map1, tournament))
    if not mp.contains(map2, year):
        #Este mapa contiene los años en los que el torneo tiene registros.
        elem = mp.newMap(200,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements)
        mp.put(map2, year, elem)

    map3=me.getValue(mp.get(map2, year))

    req6_add_team(map3, data)

    mp.put(map2, year, map3)
    mp.put(map1, tournament, map2)

    """  if not mp.contains(map3, home_team):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(map3, home_team, elem)
    else:
        k_v = mp.get(map3,home_team)
        value = me.getValue(k_v)
        lt.addLast(value, data)
        mp.put(map3, home_team, value)

    if not mp.contains(map3, away_team):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(map3, away_team, elem)
    else:
        k_v = mp.get(map3,away_team)
        value = me.getValue(k_v)
        lt.addLast(value, data)
        mp.put(map3, away_team, value) """
    
def add_score_date(data_structs, data):

    data_date = date.fromisoformat(data["date"])
    if not mp.contains(data_structs, data_date):
        elem = lt.newList("ARRAY_LIST", compare_elements)
        lt.addLast(elem,data)
        mp.put(data_structs, data_date, elem)
    else:
        k_v = mp.get(data_structs,data_date)
        value = me.getValue(k_v)
        lt.addLast(value, data)
        mp.put(data_structs, data_date, value)

def addMatchResultsByTeam(data_team,matchResult):
    teamMap= data_team["teams"]
    teamNameA=matchResult['home_team']
    entry= mp.get(teamMap,teamNameA)
    if entry:
        team= me.getValue(entry)
    else:
        team= newTeam()
        mp.put(teamMap, teamNameA, team)
    lt.addLast(team["MatchResults"]["list"],matchResult)
    data_date= date.fromisoformat(matchResult["date"])
    add_element(team["MatchResults"]["map"],matchResult,data_date)
    addMatchResultByCondition(team, matchResult,teamNameA)
    teamNameB=matchResult['away_team']
    entrys= mp.get(teamMap,teamNameB)
    if entrys:
        team= me.getValue(entrys)
    else:
        team= newTeam()
        mp.put(teamMap, teamNameB, team)
    lt.addLast(team["MatchResults"]["list"],matchResult)
    data_date= date.fromisoformat(matchResult["date"])
    add_element(team["MatchResults"]["map"],matchResult,data_date)
    addMatchResultByCondition(team, matchResult,teamNameB)



def addMatchResultByCondition(nodo, matchResult, team):
    conditionMap= nodo["matchResultsByCondition"]
    condition="away"
    if matchResult["home_team"]==team:
        condition="home"
    entry= mp.get(conditionMap, condition)
    if entry:
        conditionList= me.getValue(entry)
    else:
        conditionList= lt.newList("ARRAY_LIST")
        mp.put(conditionMap,condition, conditionList)
    lt.addLast(conditionList,matchResult)

def newTeam():
    team={}
    team["MatchResults"]={"list":lt.newList("ARRAY_LIST"), "map":mp.newMap(300,maptype="PROBING", cmpfunction=compare_elements)}
    team["matchResultsByCondition"]=mp.newMap(2,maptype="PROBING")
    return team

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
        mp.put(data_structs, data_date, value)


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


def req6_add_tournament(data_structs, data):
    tournament = data['tournament']
    year = str(date.fromisoformat(data['date']).year)
    city=data['city']
    country=data['country']
    if not mp.contains(data_structs, year):
        elem = mp.newMap(200,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements)
        mp.put(data_structs, year, elem)
    map_year = me.getValue(mp.get(data_structs,year))
    if not mp.contains(map_year, tournament):
        elem = mp.newMap(200,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements)
        mp.put(elem,'cities',mp.newMap(200,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements))
        mp.put(elem,'countries',lt.newList("ARRAY_LIST",compare_string))
        mp.put(elem, 'total_matches',lt.newList("ARRAY_LIST", compare_results_list))
        mp.put(map_year, tournament, elem)
    k_v = mp.get(map_year,tournament)
    map2 = me.getValue(k_v)
    countries = me.getValue(mp.get(map2, 'countries'))
    if not lt.isPresent(countries,country):
        lt.addLast(countries, country)
    cities = me.getValue(mp.get(map2, 'cities'))
    if not mp.contains(cities, city):
        mp.put(cities, city, 1)
    else:
        number = me.getValue(mp.get(cities, city))
        number+=1
        mp.put(cities, city, number)
    total_matches = me.getValue(mp.get(map2, 'total_matches'))
    lt.addLast(total_matches, data)
    mp.put(map2, 'total_matches',total_matches)
    
    mp.put(data_structs, tournament, map2)

def req6_add_team(data_structs, data):
    home_team = data['home_team']
    away_team = data['away_team']
    if not mp.contains(data_structs, home_team):
        elem = {'team':home_team,'total_points':0, 
                'goal_difference':0, 
                'penalty_points':0, 
                'matches':0, 
                'own_goal_points':0, 
                'wins':0, 
                'draws':0,
                'losses':0,
                'goals_for':0, 
                'goals_against':0, 
                'top_scorer':mp.newMap(1000,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements), 
                'match_info':lt.newList("ARRAY_LIST", compare_results_list)}
        mp.put(data_structs, home_team, elem)
    if not mp.contains(data_structs, away_team):
        elem = {'team':away_team,
                'total_points':0, 
                'goal_difference':0, 
                'penalty_points':0, 
                'matches':0, 
                'own_goal_points':0, 
                'wins':0, 
                'draws':0,
                'losses':0,
                'goals_for':0, 
                'goals_against':0, 
                'top_scorer':mp.newMap(1000,
                                               maptype="PROBING",
                                               loadfactor=0.5,
                                               cmpfunction=compare_elements), 
                'match_info':lt.newList("ARRAY_LIST", compare_results_list)}
        mp.put(data_structs, away_team, elem)

    home_team_dic = me.getValue(mp.get(data_structs,home_team))
    away_team_dic = me.getValue(mp.get(data_structs,away_team))
    winner = winner_determiner(data)

    if winner == 'home':
        home_team_dic['total_points']+=3
        home_team_dic['wins']+=1
        away_team_dic['losses']+=1
    elif winner =='draw':
        home_team_dic['total_points']+=1
        home_team_dic['draws']+=1
        away_team_dic['draws']+=1
        away_team_dic['total_points']+=1
    elif winner =='away':
        away_team_dic['total_points']+=3
        away_team_dic['wins']+=1
        home_team_dic['losses']+=1

    home_team_dic['goals_for']+=int(data['home_score'])
    home_team_dic['goals_against']+=int(data['away_score'])
    away_team_dic['goals_for']+=int(data['away_score'])
    away_team_dic['goals_against']+=int(data['home_score'])

    home_team_dic['goal_difference']+=(int(data['home_score'])-int(data['away_score']))
    away_team_dic['goal_difference']+=(int(data['away_score'])-int(data['home_score']))
    home_team_dic['matches']+=1
    away_team_dic['matches']+=1
    lt.addLast(home_team_dic['match_info'],data)
    lt.addLast(away_team_dic['match_info'],data)
    mp.put(data_structs,home_team, home_team_dic)
    mp.put(data_structs, away_team, away_team_dic)

def winner_determiner(data):
    #Retorna el ganador de un partido. Retorna draw si es empate.
    if data['home_score']> data['away_score']:
        return 'home'
    elif data['home_score']== data['away_score']:
        return 'draw'
    elif data['home_score']<data['away_score']:
        return 'away'
    
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

def values_to_array(data_struct):
    array_list = lt.newList("ARRAY_LIST")
    values= mp.valueSet(data_struct)
    for value in lt.iterator(values):
        lt.addLast(array_list, value)
    return array_list

def adicionar_jugador_goles(data_structs, name, data):
    
    if not mp.contains(data_structs["jugador_goles"],name):
        elem = lt.newList("ARRAY_LIST")
        lt.addLast(elem,data)
        mp.put(data_structs["jugador_goles"],name,elem)
    else:
        k_v =mp.get(data_structs["jugador_goles"],name)
        value = me.getValue(k_v)
        lt.addLast(value,data)
        mp.put(data_structs["jugador_goles"],name, value)
        
# Funciones de consulta

def get_data_3(data_structs,tamano):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista   
    resultados = lt.newList("ARRAY_LIST")
    lt.addFirst(resultados,lt.firstElement(data_structs))
    for b in range(2,4):
        p = lt.getElement(data_structs, b)
        lt.addLast(resultados, p)
    for b in range (0,3):
        p = lt.getElement(data_structs, (tamano-2+b))
        lt.addLast(resultados, p)
    return resultados


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, team, condition):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    if condition!="MatchResults":
        resultado= me.getValue(mp.get(me.getValue(mp.get(data_structs["model"]["teams"],team))["matchResultsByCondition"],condition))
    else:
        resultado= me.getValue(mp.get(data_structs["model"]["teams"],team))["MatchResults"]["list"]
    if resultado:
        total_teams= mp.size(data_structs["model"]["teams"])
        total_partidos= lt.size(me.getValue(mp.get(data_structs["model"]["teams"],team))["MatchResults"]["list"])
        return merg.sort(resultado,results_sort_criteria),total_teams,total_partidos
    else:
        return "El equipo no tiene partidos en esa condicion",0,0
def req_2(data_structs, nombre, cant_goles):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
     
    if mp.contains(data_structs["jugador_goles"], nombre):
        goles_entry = mp.get(data_structs["jugador_goles"],nombre)
        goles = me.getValue(goles_entry)
        merg.sort(goles,cmp_crit_goal_req_2)
        if lt.size(goles) >= cant_goles:
            return lt.subList(goles, 1, cant_goles)
        else: 
            return goles
    else:
        return "El jugador no existe"


#def req_3(data_structs, date_in, date_f,team):
    """
    Función que soluciona el requerimiento 3
    """
    date_inicial=date.fromisoformat(date_in)
    date_final=date.fromisoformat(date_f)
    mantener= True
    resultado= lt.newList("ARRAY_LIST")
    mapa= me.getValue(mp.get(data_structs["model"]["teams"],team))["MatchResults"]["map"]

    fecha_inicial= mpo.floor(mapa,date_inicial)
    valor_inicial=me.getValue(mp.get(mapa,fecha_inicial))
    #goal scorers 
    auto,penal=its_present_in_goal(data_structs,fecha_inicial)
    valor_inicial["penalty"]=penal
    valor_inicial["own_goal"]=auto

    fecha_final= mpo.ceiling(mapa,date_final)
    valor_final= me.getValue(mp.get(mapa,fecha_final))
    #goal scorers 
    auto_1,penal_1=its_present_in_goal(data_structs,fecha_final)
    valor_final["penalty"]=penal_1
    valor_final["own_goal"]= auto_1
    
    lt.addLast(resultado,valor_final)
    while mantener==True:
        fecha_fin = fecha_final + timedelta(days=1)
        fecha_final= mpo.ceiling(mapa,fecha_fin)
        if fecha_inicial==fecha_final:
            lt.addFirst(resultado,valor_inicial)
            mantener=False
        valor_extra= me.getValue(mp.get(mapa,fecha_final))
        auto_1,penal_1=its_present_in_goal(data_structs,fecha_final)
        valor_extra["penalty"]=penal_1
        valor_extra["own_goal"]= auto_1
        lt.addFirst(resultado,valor_extra)
    return resultado
def req_3(data_structs, date_in, date_f,team):
    """
    Función que soluciona el requerimiento 3
    """
    away_team= 0
    home_team=0
    lista=lt.newList("ARRAY_LIST")
    todos=lt.newList("ARRAY_LIST")
    date_inicial=date.fromisoformat(date_in).year
    date_final=date.fromisoformat(date_f).year
    date_inicial_fecha=date.fromisoformat(date_in)
    date_final_fecha=date.fromisoformat(date_f)
    mapa= data_structs["model"]["results"]
    resultado= mp.keySet(mapa)
    for key in lt.iterator(resultado):

        if date_final>=key and key>=date_inicial:
            valor= me.getValue(mp.get(mapa,key))
            for cada in lt.iterator(valor):
                fecha= date.fromisoformat(cada["date"])
                if date_final_fecha>=fecha and fecha>=date_inicial_fecha:

                #para todos
                    away=cada["away_team"]
                    todos = its_present_partidos(todos,away)
                    home= cada["home_team"]
                    todos = its_present_partidos(todos,home)
                    if away==team:
                        away_team+=1
                        auto,penal=its_present_in_goal(data_structs,fecha,away,"away_team")
                        cada["penalty"]=penal
                        cada["own_goal"]=auto
                        lt.addLast(lista,cada)
                    elif home==team:
                        home_team+=1
                        auto,penal=its_present_in_goal(data_structs,fecha,home,"home_team")
                        cada["penalty"]=penal
                        cada["own_goal"]=auto
                        lt.addLast(lista,cada)
    return away_team,home_team,(away_team + home_team), lt.size(todos),lista
def its_present_partidos(lista,team):
    n= lt.isPresent(lista,team)
    if n==0:
        lt.addLast(lista,team)
    return lista
def its_present_in_goal(data_structs,fecha,equipo,condicion):
    auto="unknown"
    penal="unknown"
    entry= mp.get(data_structs["model"]["goal_scorers_by_year"],fecha)
    if entry:
        entry= me.getValue(entry)
        for cada in lt.iterator(entry):
            equi= cada[condicion]
            if equi==equipo:
                if penal!="True":
                    penal=cada["penalty"]
                if auto!="True":
                    auto= cada["own_goal"]
                
    return auto,penal
        

    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs, tournament, start_d, end_d):
    start_y = date.fromisoformat(start_d).year
    end_y = date.fromisoformat(end_d).year
    map1 = data_structs['tournaments_by_year']
    year_i = start_y
    countries = lt.newList("ARRAY_LIST", compare_string)
    cities = lt.newList("ARRAY_LIST", compare_string)
    tournament_matches = lt.newList("ARRAY_LIST",compare_results_list)
    shootout_matches = 0
    while int(year_i)<=int(end_y):
        if mp.contains(map1, str(year_i)):
            map2= me.getValue(mp.get(map1, str(year_i)))
            if mp.contains(map2, tournament):
                map3 = me.getValue(mp.get(map2, tournament))
                matches = me.getValue(mp.get(map3, 'total_matches'))
                for match in lt.iterator(matches):
                    if start_d<match['date']<end_d:
                        match['winner']='Unavailable'
                        lt.addLast(tournament_matches, match)
                        if not lt.isPresent(countries, match['country']):
                            lt.addLast(countries, match['country'])
                        if not lt.isPresent(cities, match['city']):
                            lt.addLast(cities, match['city'])

        year_i= str(int(year_i)+1)
    
    shootouts = data_structs['shootouts_date']
    merg.sort(tournament_matches, req4_sort_criteria)
    for match in lt.iterator(tournament_matches):
        m_date = date.fromisoformat(match['date'])
        if mp.contains(shootouts, m_date):
            shootout_list= me.getValue(mp.get(shootouts, m_date))
            shootout = lt.isPresent(shootout_list,match)
            if shootout:
                shootout_matches+=1
                winner=lt.getElement(shootout_list, shootout)['winner']
                match['winner']=winner
    n_tournaments = mp.size(data_structs['teams_tournament_year'])
    n_matches = lt.size(tournament_matches)
    n_countries = lt.size(countries)
    n_cities = lt.size(cities)

    return tournament_matches, n_tournaments, n_matches, n_countries, n_cities, shootout_matches

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


def req_6(data_structs, n_teams, tournament, year):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    map_tournament = me.getValue(mp.get(data_structs['teams_tournament_year'],tournament))
    scores_date = data_structs['scores_date']
    map_year = me.getValue(mp.get(map_tournament, year))
    teams = values_to_array(map_year)
    
    for team in lt.iterator(teams):
        matches = lt.iterator(team['match_info'])
        for match in matches:
            home_team = match['home_team']
            away_team = match['away_team']
            m_date = date.fromisoformat(match['date'])
            if mp.contains(scores_date,m_date):
                #Se encarga de mirar quiénes marcaron un gol en un partido específico. 
                #Esto para asegurar que el número de goles y partidos sean distintos (un jugador pudo haber marcado más de un gol en un partido)
                scorer_list=lt.newList("ARRAY_LIST")
                scores =me.getValue(mp.get(scores_date, m_date))
                for score in lt.iterator(scores):
                    if score['home_team']==home_team and score['away_team']==away_team:
                        scorer = score['scorer']
                        if not lt.isPresent(scorer_list, scorer):
                            lt.addLast(scorer_list, scorer)
                        if not mp.contains(team['top_scorer'],scorer):
                            elem={"scorer":scorer, "goals":1, 'matches':0, 'avg_time':float(score['minute'])}
                            mp.put(team['top_scorer'],scorer, elem)
                        else:
                            dic = me.getValue(mp.get(team['top_scorer'],scorer))
                            dic['goals']+=1
                            dic['avg_time']= ((dic['avg_time']*(dic['goals']-1))+float(score['minute']))/dic['goals']
                            mp.put(team['top_scorer'],scorer, dic)
                        if score['own_goal']=="True":
                            team['own_goal_points']+=1
                        if score['penalty']=="True":
                            team['penalty_points']+=1

                for scorer in lt.iterator(scorer_list):
                    dic = me.getValue(mp.get(team['top_scorer'],scorer))
                    dic['matches']+=1
                    mp.put(team['top_scorer'],scorer, dic)
    merg.sort(teams, req6_sort_criteria)
    size = lt.size(teams)
    if n_teams>size:
        first_teams = teams
    else:
        first_teams = lt.subList(teams,1,n_teams)
    
    total_years = mp.size(map_tournament)
    year_info = me.getValue(mp.get(data_structs['tournaments_by_year'],str(year)))
    total_tournaments = mp.size(year_info)
    n_teams_y = lt.size(teams)
    tournament_info = me.getValue(mp.get(year_info,tournament))
    total_matches = lt.size(me.getValue(mp.get(tournament_info, 'total_matches')))
    n_countries = lt.size(me.getValue(mp.get(tournament_info,'countries')))
    cities = me.getValue(mp.get(tournament_info, 'cities'))
    n_cities = mp.size(cities)
    k_vs = lt.newList("ARRAY_LIST")
    for key in lt.iterator(mp.keySet(cities)):
        lt.addLast(k_vs, mp.get(cities,key))
    merg.sort(k_vs, pop_city_sort_criteria)
    pop_city = me.getKey(lt.firstElement(k_vs))
    return first_teams,total_years, total_tournaments, n_teams_y, total_matches, n_countries, n_cities, pop_city



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


def scorers_sort_criteria(data1, data2):
    if int(data1['goals'])>int(data2['goals']):
        return True
    elif data1['goals']==data2['goals'] and float(data1['avg_time'])<float(data2['avg_time']):
        return True
    return False

def compare_elements(keyname, element):
    shootout_entry = me.getKey(element)
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

    
def cmp_req_2_final(key_name, jugador_goles_entrada):
    nombre_entrada = me.getKey(jugador_goles_entrada)
    if key_name == nombre_entrada:
        return 0
    elif key_name > nombre_entrada:
        return 1
    else:
        -1
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

def compare_string(data_1, data_2):
    if data_1 == data_2:
        return 0
    elif data_1>data_2:
        return 1
    return -1

def pop_city_sort_criteria(data1, data2):
    if data1['value']>data2['value']:
        return True
    return False
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

def dates_new_first_criteria(data1, data2):
    if data1>data2:
        return True
    return False

def cmp_crit_goal_req_2(data_1, data_2):
    date_1 = date.fromisoformat(data_1["date"])
    date_2 = date.fromisoformat(data_2["date"])
    
    mn_1 = float(data_1["minute"])
    mn_2 = float(data_2["minute"])
    
    if date_1 > date_2:
        if mn_1 > mn_2:
            return True
        return False
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

def sort_dates_new_first(list):
    merg.sort(list, dates_new_first_criteria)

def sort_players_req6(data_struct):
    merg.sort(data_struct, sort_p6_sort_criteria)

def req4_sort_criteria(data1, data2):
    date1= date.fromisoformat(data1['date'])
    date2= date.fromisoformat(data2['date'])
    if date1>date2:
        return True
    elif date1==date2 and data1['country']<data2['country']:
        return True
    elif date1==date2 and data1['country']==data2['country'] and data1['city']<data2['city']:
        return True
    return False

def req6_sort_criteria(data1, data2):
    if data1['total_points']>data2['total_points']:
        return True

    elif data1['total_points']==data2['total_points'] and data1['goals_for']>data2['goals_for']:
        return True
    
    elif data1['total_points']==data2['total_points'] and data1['goals_for']==data2['goals_for'] and data1['penalty_points']>data2['penalty_points']:
        return True
    
    elif data1['total_points']==data2['total_points'] and data1['goals_for']==data2['goals_for'] and data1['penalty_points']==data2['penalty_points'] and data1['goals_against']<data2['goals_against']:
        return True

    elif data1['total_points']==data2['total_points'] and data1['goals_for']==data2['goals_for'] and data1['penalty_points']==data2['penalty_points'] and data1['goals_against']==data2['goals_against'] and data1['own_goal_points']<data2['own_goal_points']:
        return True
    return False

def sort_p6_sort_criteria(data1, data2):
    if data1['goals']>data2['goals']:
        return True
    elif data1['goals'] ==data2['goals'] and data1['avg_time'] <data2['avg_time']:
        return True
    return False

    
