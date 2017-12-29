import sys

from funciones_adicionales import reserva_clase
import logging

logging.basicConfig(filemode='w', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()

name = sys.argv[1]
reserva_clase(name)