import datetime
from model.aplicacao import Aplicacao
from model.configuracao import Configuracao
import os

class Backup():

    def __init__(self, config: Configuracao, app: Aplicacao) -> None:
        self.__data = datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
        self.__dst_folder = os.path.join(config.src_backup, app.nome, self.__data)
        self.__src = os.path.join(config.src_tomcat, app.nome)
        self.__dst = os.path.join(self.__dst_folder, app.nome)

    @property
    def src(self):
        return self.__src

    @property
    def dst(self):
        return self.__dst

    @property
    def dst_folder(self):
        return self.__dst_folder