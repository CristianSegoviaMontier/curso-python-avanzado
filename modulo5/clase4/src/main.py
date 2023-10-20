from prefect import flow
import logging
import warnings
from tasks.get_offers import(  # estoy llamndo el modulo (que es una carpeta ) y su sub modulo (que es el archi .py)
    get_offers
)
from tasks.save_offers import(
    save_offers
)

# Suprime todas las advertencias
warnings.filterwarnings("ignore")


log = logging.getLogger()

SKILL = 'python'

@flow(name='EXTRAER OFERTA LABORAL LINKEDIN')  # flow es un decorador = Es una funcion que llama otra funcion, agregando funcionalidad
def main_flow():
    log.info(f'PROCESO DE EXTRACCION')
    offers = get_offers(SKILL)
    save_offers(offers)
    # print(offers)


if __name__ == '__main__':
    main_flow()
