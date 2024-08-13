# djbs-theme
Django Admin Bootstrap theme

djbs is a theme for django-admin based on the bootstrap framework. It is an adaptation of the django.contrib.admin app templates and the django.forms templates to use bootstrap components.

Versions:
- Python=3.12.3
- Django=5.1
- Bootstrap=5.3

To set up a development environment (assuming you have an Ubuntu installation with Python3 already installed):
  - Install the venv module:
    $ sudo apt update && sudo apt install python3-venv
  - Create the project directory:
    $ mkdir djbs-theme && cd djbs-theme
  - Create a virtualenv in the project:
    $ python3 -m venv .venv/djbs-theme
  - Activate the virtualenv:
    $ source .venv/djbs-theme/bin/activate
  - Install the necessary python packages:
    $ pip install pip ipython django pyYaml django-debug-toolbar --upgrade
  - Create the django-project:
    $ django-admin startproject djbstheme .
  - Clone this repository into your project:
    $ git clone https://github.com/interlegis/djbs-theme.git djbs
  - Configure the project by changing the application's settings.py.
    - Use your preferred text editor to edit the ./djbstheme/settings.py file:
    - Find the INSTALLED_APPS list and add, before the 'django.contrib.admin' app, the 'djbs' and 'django.forms' app
    - Add the FORM_RENDERER = 'django.forms.renderers.TemplatesSetting' configuration

That's it! Your project is configured.

---

djbs é um tema para o django-admin baseado no framework bootstrap. É uma adaptação dos templates do app django.contrib.admin e dos templates do django.forms para utilizar os componentes do bootstrap.

Versões:
  - Python=3.12.3
  - Django=5.1
  - Bootstrap=5.3
  
Para montar um ambiente de desenvolvimento (considerando que você tem uma instalação Ubuntu com Python3 já instalado):
  - Instalar o módulo venv:
    $ sudo apt update && sudo apt install python3-venv
  - Criar o diretório do projeto:
    $ mkdir djbs-theme && cd djbs-theme
  - Criar um virtualenv no projeto:
    $ python3 -m venv .venv/djbs-theme
  - Ativar o virtualenv:
    $ source .venv/djbs-theme/bin/activate
  - Instalar os pacotes python necessários:
    $ pip install pip ipython django pyYaml django-debug-toolbar --upgrade
  - Criar o django-project:
    $ django-admin startproject djbstheme .
  - Clonar este repositório dentro do seu projeto:
    $ git clone https://github.com/interlegis/djbs-theme.git djbs
  - Configure o prjeto alterando settings.py da aplicação.
    - Utilize o editor de texto de sua preferência para editar o arquivo ./djbstheme/settings.py:
    - encontre a lista INSTALLED_APPS e acrescente, antes da app 'django.contrib.admin', a app 'djbs' e 'django.forms'
    - Adicione a configuração FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
    
Pronto! Seu projeto está configurado.