![shield](https://img.shields.io/github/last-commit/Cocorico84/softdesk)
![shield](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![shield](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![shield](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![shield](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)
![shield](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![shield](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)

# Description

SoftDesk is an application to monitor and follow a project with its issues.

You can:
* create an account
* create a project
* follow a project
* create issues

# Prerequisites

Python 3

# Installation

To clone the repository, you can download the zip or clone either HTTPS or SSH. And when you are in the repository you can activate your virtual environement.

On Linux or Mac
```shell
$ pip install virtualenv
$ virtualenv venv --python=python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

On Windows
```bat
c:\Python38\python -m venv c:\path\to\myenv
C:\\{venv}\\Scripts\\activate.bat
pip install -r requirements.txt
```

# Quickstart

To create a superuser:
```console
python manage.py createsuperuser
```
This will allow you to connect to the admin panel.

To see the website in local, run this command :

```console
python manage.py runserver
```
When you launch this command, it will start the website on http://127.0.0.1:8000.
You can create a user or you can login if you have already created one.

You can also create users from shell:
```py
python manage.py shell
from django.contrib.auth.models import User
User.objects.create_user('foo', password='bar')
```
If you want to give some permissions:
```py
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user('foo', password='bar')
user.is_superuser=True
user.is_staff=True
user.save()
```
# Code Style
```
flake8 .
```
To get a report. It will create a directory named "flake8-report". Then you can open index.html in a browser.
```
flake8 --format=html --htmldir=flake8-report
```

# Contributor

If you have any suggestions to improve the project, you can create an issue.
