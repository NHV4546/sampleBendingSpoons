from typing import NamedTuple
from datetime import datetime, date
import csv
from collections import defaultdict
Equipo = NamedTuple("Equipo",[("nombre", str),("puntos", int),("faltas", int)])
PartidoBasket = NamedTuple("PartidoBasket",[("fecha", date), ("competicion", str), ("equipo1", Equipo), ("equipo2", Equipo)])
def parsea_y_suma_resultados(cadena: str) -> tuple[int, int]:
    lista = cadena.split('*')
    sum1 = 0
    sum2 = 0
    for i in lista:
        sum1+= int(i.split('-')[0])
        sum2+= int(i.split('-')[1])
    return (sum1, sum2)

def lee_partidos(fichero: str)-> list[PartidoBasket]:
    res = []
    with open(fichero, 'rt', encoding = 'UTF-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for fecha,equipo_1,equipo_2,torneo,cuartos,faltas_1,faltas_2 in lector:
            equipo1 = Equipo(equipo_1, parsea_y_suma_resultados(cuartos)[0], int(faltas_1))
            equipo2 = Equipo(equipo_2, parsea_y_suma_resultados(cuartos)[1], int(faltas_2))
            date0 = datetime.strptime(fecha, '%d/%m/%Y').date()
            res.append(PartidoBasket(date0, torneo, equipo1, equipo2))
    return res
