# Django Menu

Tree menu layout for django application

# How to deploy
You can run the project in docker, but then you have to manually 
provides data in database via Django admin or use my sqlite3 file, but run project
via creating venv and runserver manually

###  Via docker
1. Clone the repository
```commandline
git clone https://github.com/GCTMLP/django_menu.git
```
2. Go to folder
```commandline
cd django_menu
```
3. Run docker containers
```commandline
docker-compose  up -d --build
```
4. Enjoy on http://127.0.0.1:8000/

###  Via runserver

1. Clone the repository
```commandline
git clone https://github.com/GCTMLP/django_menu.git
```
2. Go to folder
```commandline
cd django_menu
```
3. Create venv and activate
```commandline
 python3 -m venv my_venv
 source my_venv/bin/activate
```
4. Install packages
```commandline
pip3 install -r requirements.txt 
```
5. Make migrations
```commandline
python3 manage.py makemigrations
python3 manage.py migrate
```
6. Runserver
```commandline
python3 manage.py runserver
```
7. Enjoy on http://127.0.0.1:8000/



