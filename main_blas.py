from splinter import Browser
import time
import random
import datetime
from funciones_adicionales import reserva_primera_clase
import logging
from profiles import get_profiles

logging.basicConfig(filemode='w', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

list_days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo',
             'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']


from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()


def main():
    line = "vladisimon@gmail.com|abc123456+"
    wait_time = 4
    profiles, assign_profiles = get_profiles()
    single_profile = profiles[assign_profiles['blas']]
    position_class = single_profile + single_profile
    weekday = datetime.datetime.today().weekday()
    reserva_primera_clase(line, weekday, wait_time, position_class)


main()