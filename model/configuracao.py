import configparser
import os

class Configuracao():

    def __init__(self) -> None:
        self.__config = configparser.ConfigParser()
        self.__config.sections()
        self.__config.read(os.path.join('conf', 'configuracao.ini'))

        if(self.__config.has_option('Configs', 'src.tomcat')):
            self.__src_tomcat = self.__config['Configs']['src.tomcat']
        else:
            raise Exception('Não foi possivel encontrar a configuração src.tomcat')
        
        if(self.__config.has_option('Configs', 'src.backup')):
            self.__src_backup = self.__config['Configs']['src.backup']
        else:
            raise Exception('Não foi possivel encontrar a configuração src.backup')
        
        if(self.__config.has_option('Configs', 'src.webinf')):
            self.__src_webinf = self.__config['Configs']['src.webinf']
        else:
            raise Exception('Não foi possivel encontrar a configuração src.webinf')

        if(not os.path.exists(self.__src_tomcat)):
            raise Exception('scr do tomcat não existe\nverifique o arquivo conf/configuracao.ini')
        
        if(not os.path.exists(self.__src_backup)):
            raise Exception('scr do backup não existe\nverifique o arquivo conf/configuracao.ini')
        
        if(not os.path.exists(self.__src_webinf)):
            raise Exception('scr do WEB-INF não existe\nverifique o arquivo conf/configuracao.ini')

    @property
    def src_tomcat(self):
        return self.__src_tomcat

    @property
    def src_backup(self):
        return self.__src_backup

    @property
    def src_webinf(self):
        return self.__src_webinf