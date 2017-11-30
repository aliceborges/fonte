# Projeto de Desenvolvimento Web II
###### IFC - Araquari / 2017
###### Projeto desenvolvido em ambiente Linux, programa PyCharm e front-end feito no Pingendo.
###### Site para download de fontes gratuito.

### Comandos

#### 1. Baixar o repositório:
```
git clone https://github.com/aliceborges/fonte
```


#### 2. Instalar/Verificar se tem Virtualenvwrapper na máquina:
```
sudo apt install virtualenvwrapper
mkvirtualenv fonte
workon fonte
```

#### 3. Entrar na pasta do projeto e instalar as dependências:
```
pip freeze
pip install Django==1.9
pip install Pillow
pip freeze > /requirements.txt
cat requirements.txt
```

#### 4. Migrar o SQLite

```
cd fonte
python manage.py makemigrations
python manage.py migrate
```

#### 5. Rodar o projeto no navegador
```
python manage.py runserver
```


### Observações


#### Adicionar contribuidores no contributors.txt:
```
echo “Alice Borges” >> contributors.txt
```

#### Commit:
```
git status
git add .
git commit -m ""
git push -u origin master
```

#### Desenvolvendo com o PyCharm:

```
Abrir o projeto
Fazer as devidas alterações
Crtl + k para commitar
```
