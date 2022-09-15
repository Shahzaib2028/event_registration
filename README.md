# Event Management



[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Install all requirements

You can find **requirements.txt** file in root directory of the project. Use this command for installation

``` pip3 install -r requirements.txt```

## create super user

To create a super user use this command:

``` python3 manage.py createsuperuser```

or you can also create super user, using shell by following these commands.

```
python3 manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
user = User()
user.username = "username"
user.name = "name"
user.set_password("password")
user.is_staff = True
user.is_active = True
user.is_superuser = True
user.mobile_number = "033xxxxxx87"
user.save()
exit()
```


## Set Database

You can find settings in **./config/settings/base.py**

here you find the code block for **DATABASES**

```
DATABASES={
   'default':{
      'ENGINE':'django.db.backends.postgresql_psycopg2',
      'NAME':'postgres',
      'USER':'postgres',
      'PASSWORD':'xxxxxxxx',
      'HOST':'localhost',
      'PORT':'5433',
   }
}

```

## Now Run the localhost

To run you app just use the command

```python3 manage.py runserver```

or you can also give specific port number as well by using command

```python3 manage.py runserver <port no.>```

# URLs Information

## To register a new User

If user wants to register/signup then go to URL.

```http://127.0.0.1:<port no>/registration/register/```

## Login 

If user wants to login then go to URL.

```http://127.0.0.1:<port no>/registration/login/```

## Logout

If user wants to logout then go to URL.

```http://127.0.0.1:<port no>/registration/logout/```

## Show/GET all existing Events

If user wants to see all existing events then go to the URL:

```http://127.0.0.1:<port no>/event/```


## Show/GET single existing Event

If user wants to see a specific event then to go URL.

```http://127.0.0.1:<port no>/event/retrieve/<id>/```


In **id** you need to give the unique id of that event

## Create an Event

If user wants to create a new event then user **must need to login first** and then go to URL.

```http://127.0.0.1:<port no>/event/create/```

## Update an Event

If user wants to update the event then user **must need to login first** and then go to URL.

```http://127.0.0.1:<port no>/event/<id>/```

- In **id** user need to give the unique id of created event

- Only the owner who created the event can update the event

## Delete an Event


If user wants to delete the event then user **must need to login first** and then go to URL.

```http://127.0.0.1:<port no>/event/<id>/```

- In **id** user need to give the unique id of created event

- Only the owner who created the event can delete the event

## Attend an Event

If user want to attend the event then user **must need to login first** and then go to URL.

```http://127.0.0.1:<port no>/event/attend/<id>/```

In **id** user need to give the unique id of the event which user wants to attend.


### To run the test cases

Test cases are created in two apps 1) user.  2) manage_event

To run all the test cases use the command.

```python3 manage.py test```

To run test cases of the specific app use command

```python3 manage.py test <app name>```


### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
