from model.aplicacao import Aplicacao
from model.configuracao import Configuracao
import os

class WebInf():

    def __init__(self, config: Configuracao, app: Aplicacao) -> None:
        self.__src_folder = config.src_webinf
        self.__dst_folder = os.path.join(app.dst, 'WEB_INF')
        self.__src = os.path.join(self.__src_folder, 'rewrite.config')
        self.__dst = os.path.join(self.__dst_folder, 'rewrite.config')

    @property
    def src_folder(self):
        return self.__src_folder

    @property
    def src(self):
        return self.__src
    
    @property
    def dst_folder(self):
        return self.__dst_folder

    @property
    def dst(self):
        return self.__dst