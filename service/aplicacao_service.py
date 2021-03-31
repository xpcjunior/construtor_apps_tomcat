from util.barra_de_progresso import BarraDeProgresso
from model.aplicacao import Aplicacao
import os, shutil
import time

class AplicacaoService():
    
    @staticmethod
    def executar_deploy(app: Aplicacao):
        
        print('====================================================')
        print('Executando deploy da aplicação')
        print('====================================================')

        if (os.path.isdir(app.src)):
            shutil.copytree(app.src, app.dst, symlinks=False, ignore=None)
        else:
            shutil.copyfile(app.src, app.dst)
        
        BarraDeProgresso.print(0, 30, prefix = 'Progresso:')

        for seq in range(0, 30):
            BarraDeProgresso.print(seq + 1, 30, prefix = 'Progresso:')
            time.sleep(0.1)
            
        print('Deploy executado com sucesso!')
