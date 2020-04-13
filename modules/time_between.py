"""
    Este modulo se encarga de los tiemops
"""
import datetime as date
def time_between(last_update_string):
    """
        Retorna verdadero si ha pasado 30 minutis
        antes de la ultima actualización de un invocador.
        En caso contrario, retornará falso
    """
    now = date.datetime.now()
    last_update = date.datetime.strptime(last_update_string, "%d/%m/%Y %H:%M:%S") #24

    delta = now - date.timedelta(minutes=30)

    if delta >= last_update:
        return True
    else:
        return False
