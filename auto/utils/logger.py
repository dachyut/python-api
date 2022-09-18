import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="auto.log")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger