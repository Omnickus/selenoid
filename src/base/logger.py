import logging
import config
import random
import os


class Logger:
    
    __name = 'Класс для логирования'

    level_log_for_print = ''

    __list_log_level = {
        'CRITICAL' : 50,
        'ERROR' : 40,
        'WARNING' : 30,
        'INFO' : 20,
        'DEBUG' : 10,
    }
    
    __logger = logging.getLogger(config.logger_name)
    __logger.setLevel(__list_log_level[config.log_level])
    __loglevel = __logger.getEffectiveLevel()
    
    a = os.path.basename(__file__)
    b = os.path.abspath(__file__).replace(a, '')
    __fh = logging.FileHandler( str(b) + '/logs/' + config.logger_file_name)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    __fh.setFormatter(formatter)

    def __init__(self, message = None):
        self.__message = message

    @property
    def infolog(self):
        self.__logger.addHandler(self.__fh)
        self.__logger.info(self.__message)

    @property
    def errorlog(self):
        self.__logger.addHandler(self.__fh)
        self.__logger.error(self.__message)

    @property
    def debuglog(self):
        if self.__loglevel == 10:
            self.__logger.addHandler(self.__fh)
            self.__logger.debug(self.__message)
        

