from model.aplicacao import Aplicacao
from model.backup import Backup
from model.configuracao import Configuracao
from model.webinf import WebInf
from service.aplicacao_service import AplicacaoService
from service.backup_service import BackupService
from service.webinf_service import WebInfService
import sys


def main(argv):

    try:
        configuracoes = Configuracao()
        app_para_deploy = Aplicacao(argv, configuracoes)
        backup_app = Backup(configuracoes, app_para_deploy)

        BackupService.executar_backup(backup_app)
        AplicacaoService.executar_deploy(app_para_deploy)

        if(app_para_deploy.isdir):
            wi = WebInf(configuracoes, app_para_deploy)
            WebInfService.criar_web_inf(wi)

    except Exception as erro:
        print('=================================================')
        print('Falha ao executar Script')
        print('=================================================')
        print(erro)
        print('=================================================')
        exit()

    

if __name__ == "__main__":
   main(sys.argv[1:])