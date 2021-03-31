# Construtor de Apps no Tomcat

Este projeto feito em Python 3 tem como objetivo fazer o deploy automático de aplicações JAVA em um servidor de aplicação TOMCAT.
## MAS
Se você usar sua criatividade ele pode ser utilizado para fazer o deploy de uma porrada de App em uma porrada de servidor de aplicação.

## Usabilidade

```
python main.py <arquivo ou pasta para deploy>
```

## Configuração

Antes de sair rodando o comando acima no console é bom você configurar as váriaveis contidas no arquivo [conf/configuracao.ini](conf/configuracao.ini)

## Mas o que acontece mesmo?

1) É verificado se existe um app com o mesmo nome na pasta webapps do tomcat se sim é feito um backup do mesmo, movendo-o para dentro de uma pasta com data dentro da pasta de backup.

2) O arquivo ou pasta que vc passou como parâmentro será copiado para dentro da pasta webapps do Tomcat.

3) Caso seja uma pasta que você tenha passado será verificado se a pasta WEB-INF esta dentro dela, caso não esteja, será copiada a pasta modelo em [conf/WEB-INF](conf/WEB-INF).