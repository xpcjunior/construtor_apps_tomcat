from model.configuracao import Configuracao
import os

class Aplicacao():

    def __init__(self, argv, config: Configuracao) -> None:
        if(len(argv) != 1):
            raise Exception('Parametros incorretos\nusabilidade: main.py <arquivo war ou pasta para deploy>')
        else:
            if(not os.path.exists(argv[0])):
                raise Exception(f'O arquivo: {argv[0]}  não existe')

        self.__nome = os.path.basename(argv[0])
        self.__src = argv[0]
        self.__dst = os.path.join(config.src_tomcat, self.__nome)
        self.__isdir = os.path.isdir(self.__src)

    @property
    def nome(self):
        return self.__nome

    @property
    def src(self):
        return self.__src

    @property
    def dst(self):
        return self.__dst

    @property
    def isdir(self):
        return self.__isdir