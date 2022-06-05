import logging

logger = logging

logger.basicConfig(filename="inventory_1.log",level=logging.INFO,
            format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

logger.basicConfig(filename="nventory_1.log",level=logging.ERROR,
            format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineo)d')