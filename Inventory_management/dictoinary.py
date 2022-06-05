
from distutils.log import info
from LoggerHandler import logger

class IngDict:
    def paractice_dict(self):
        try:
            d = {
                'rice' : {
                    "name":'Basmati',
                    "Price/kg" : 50
                }
            }

            total_price = 2400
            logger.info(f"Total price is calculated {total_price}")
            # c = {}

            for key,value in d.items():
                logger.info(f"Key and values{key} and {value}")
                c[key] = value

            c['rice']['total price'] = total_price
            logger.info(f"The dictionary created is {c}")

            logger.info("Program successfully worked")
        except Exception as e:
            logger.error(f"Error occured {e}")

if __name__ == "__main__":
    ing = IngDict()
    ing.paractice_dict()