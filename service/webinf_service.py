from util.barra_de_progresso import BarraDeProgresso
from model.webinf import WebInf
import os, shutil
import time

class WebInfService():

    @staticmethod
    def criar_web_inf(webinf: WebInf):

        print('====================================================')
        print('Verificando pasta WEB-INF')
        print('====================================================')


        if (not os.path.exists(webinf.dst_folder)):
            shutil.copytree(webinf.src_folder, webinf.dst_folder, symlinks=False, ignore=None)
        else:
            if (not os.path.exists(webinf.dst)):
                shutil.copyfile(webinf.src, webinf.dst)

        BarraDeProgresso.print(0, 30, prefix = 'Progresso:')

        for seq in range(0, 30):
            BarraDeProgresso.print(seq + 1, 30, prefix = 'Progresso:')
            time.sleep(0.1)
            
        print('WEB-INF verificado com sucesso!')