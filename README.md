## Introdução ##
Projeto em Python/Django para a criação de um portal dos Cursos de Extensão do DEL da UFRJ.

#### Requerimentos ####
> python 2.7.x
> pip (vem com a instalação do python. Mais detalhes: http://pip.readthedocs.org/en/latest/installing.html)
> Django 1.7 (já no requirements do projeto)
> mysql 5.5.x (ou alguma versão mais nova)

#### Instalação das dependências do projeto em ambiente local ####
> É altamente recomendável o uso de virtualenv na configuração e
> execução do projeto. Para mais informações, consulte a página oficial:
> http://virtualenv.readthedocs.org

```shell
$ pip install -r requirements.txt
```
#### Configuração do banco de dados local ####
```shell
$ mysql -u root
mysql> CREATE DATABASE cursodeextensao;
mysql> CREATE USER 'cursodeextensao'@'localhost' IDENTIFIED BY '#!Q@W#ER';
mysql> GRANT ALL PRIVILEGES ON cursodeextensao.* TO 'cursodeextensao'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> exit;
```
É necessário que se crie um superuser para iniciar a trabalhar no sistema como admin.
#### Executar o projeto ####
```shell
$ python manage.py migrate    # Cria o banco de dados e todas as tabelas
$ python manage.py runserver  # Executa a aplicação no servidor de desenvolvimento
```
#### Deploy para o ambiente de produção ####
No path ~/.ssh, execute o segundo comando (o ip no comando é o ip da máquina de produção):
```shell
ssh-keygen -R 104.131.39.168
```
Para realizar deploy em um ambiente novo, execute o seguinte comando:
```shell
$ fab prod deploy:setup=True
```
> O arquivo fabfile/environments.py é o módulo responsável pela configuração
> de ambientes. Neste módulo é onde fica o host, user e endereço da key de
> deploy, havendo possibilidade de acrescentar a senha de acesso.
> Para mais informações:
> http://docs.fabfile.org/en/1.10/usage/env.html#environment-as-configuration

Caso o deploy seja em um ambiente já configurado, execute o seguinte comando:
```shell
$ fab prod deploy
```
