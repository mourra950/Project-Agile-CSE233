# ASEC MIU student activity website

This is a university project of the Agile CSE233 course with supervision of Dr Salwa.

![image](https://user-images.githubusercontent.com/64339763/212529256-cc91cba2-5e2c-43bc-a262-69f6f22fb85f.png)

# Project Description

our objectives in this project was to find a charity or a non profitable organization to provide them with a working software that will contribute in helping their cause.
while working we were required to work and practice using the Agile mindset and started using new tools to reach higher level of teamwork and effeciency.

# Tools used

## Prototyping

we used adobe XD and DrawIO in order to draw the first Prototype of the website to show it to the client during our weekly meeting and listened to their comments to draw a better one.

![image](https://user-images.githubusercontent.com/64339763/212529427-9555aa9a-0cdd-4153-b24f-ccd0580c9ec8.png)


## Agile softwares

during this project we were introduced to new softwares like trello and jira which coordinated the tasks between our team members and divide our to work to sprints of tasks.

![image](https://user-images.githubusercontent.com/64339763/212529517-23a2a4d3-7e6e-4eed-bcba-9edea1b68fdb.png)


## Webdev

before starting we started looking for the best backend that can suit our needs and easy to use and in this case it was Django aside being written in python with good documentation it made it easier to make any changes on the long run with the least effort needded either changes in the DB or in the webpages.
for django documentation : <a href="https://www.djangoproject.com/"> Django documentation</a>

## DB

we used the django DB in managing our DB and choosed SQLite as the output to be able to access it easily and being able to share it between us without the need to configure the enviroment
but in case the client wished to change it to anything else it will be as easy as changing one line.

# Dependencies

The only thing needed to run the project is python and the Django library.
To install it you can use the following command in the terminal.

```ssh
pip install django
```

# Usage

To run the website as a local server run

```ssh
cd Agile_Project
```

then excute

```ssh
python manage.py runserver
```

then press on the url that will be provided by django to access the development server.
it will be something similar to :
```ssh
January 03, 2023 - 09:35:50
Django version 4.1.3, using settings 'Agile.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
# Note

In case you want to login as an admin input in the username textarea 'admin', and in the password 'admin'.

you can see database scheme from db file can be opened by sqlite app or you can make yourself super user by excuting in the terminal.

```ssh
python manage.py createsuperuser
```

and type in the url during running site

```ssh
www.siteurl/admin
```

to be able to access registered
modeles and directly change and see data.
