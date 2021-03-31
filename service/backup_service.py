from util.barra_de_progresso import BarraDeProgresso
from model.backup import Backup
import os, shutil
import time

class BackupService:

    @staticmethod
    def executar_backup(bkp: Backup):
        
        print('====================================================')
        print('Executando backup da aplicação')
        print('====================================================')

        if(os.path.exists(bkp.src)):
            if(not os.path.exists(bkp.dst_folder)):
                os.makedirs(bkp.dst_folder)
            shutil.move(bkp.src, bkp.dst)

            BarraDeProgresso.print(0, 30, prefix = 'Progresso:')

            for seq in range(0, 30):
                BarraDeProgresso.print(seq + 1, 30, prefix = 'Progresso:')
                time.sleep(0.1)
            print('Backup executado com Sucesso!')
        else:
            print('Sem Backup para ser realizado!')