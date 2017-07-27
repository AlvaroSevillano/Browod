from splinter import Browser
import time
import random
import datetime
from funciones_adicionales import reserva_primera_clase

import logging

logging.basicConfig(filemode='w', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

list_days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo',
             'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']


from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()


def main():
    line = "juanfrcarro@gmail.com|jonas47352436j"
    position_class = [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]
    wait_time = 6
    weekday = datetime.datetime.today().weekday()
    reserva_primera_clase(line, weekday, wait_time, position_class)


main()