# SoftDesk


1. Introduction

SoftDesk is a RESTful API to track problems about web apps, Android apps and IOS apps.

It allows the registration and authentification of users to create new projects, update them or delete them.
Users can add issues concerning these projects, and add comments about these issues.

You can read its documentation at the following link :

https://documenter.getpostman.com/view/18790689/UVREkkEq


2. Install the app 

- Download the ZIP files and unzip them in the repository you wish
- Install venv by typing in your terminal :
```
pip install venv
```
- Create de the virtual environement and launch it by typing :
```
python -m venv env
```
and
```
env\Scripts\activate
```
- install the packages by typing :
```
pip install -r requirements.txt
```


3. Launch the server

Go to the "SoftDesk" repository then type in :
$ python manage.py runserver

You can then access the site via your web browser at the following URL:
http://127.0.0.1:8000/api/signup/


4. Using the app

You can now register a new user and use the app following instructions from its documentation.

