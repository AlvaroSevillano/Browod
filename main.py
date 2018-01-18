import sys

from funciones_adicionales import reserva_clase
import logging

logging.basicConfig(filemode='w', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

name = sys.argv[1]
dev = int(sys.argv[2])

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))

if not dev:
    display.start()

reserva_clase(name, dev)
