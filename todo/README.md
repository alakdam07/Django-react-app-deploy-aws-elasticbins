# Deploy Django React app to AWS Elastic Beanstalk

 step: 1

 First create Directory
```
mkdir AppFolder && cd AppFolder
```

 step: 2

Create virtual environment
```
python3 -m venv env
```

 step: 3

 Activate the virtual environment
```
source env/bin/activate

```

step: 5

Install packages
```
pip3 install django djangorestframework django-cors-headers
```

 step: 6

Create Project
```
django-admin startproject projectname
```

step: 7

 Test the project
```
cd projectname && python3 manage.py runserver
```

step: 8

create an app

```
django-admin startapp appname
```

 step: 9

Setup eslasticBeanstalks

```
mkdir mkdir .ebextensions && touch django.config
```

 step: 10

cofigure the eslasticBeanstalks's `django.config` and paste the below code
```
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: projectName/wsgi.py
```

 step: 11

deactivate the project then inside the project-folder
```
eb init -p python-3.6 django-tutorial --region us-east-1
```

<div class="text-orange mb-2">
  PS: First delete the database from project settings. Delete this database
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'article',
        'USER': 'postgres',
        'PASSWORD': 'Joymaaloknath123',
        'HOST': 'database-2.ctrjrfmspj1h.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}

</div>

step: 12

 Create  elasticbeans environment
```
eb create django-env

```

step: 13

<div class="text-orange mb-2">
    Paste the envirnment URL in the Project settings' `Allow_HOST`

   ALLOWED_HOSTS = ['todo-deploy.eba-9nb6wjcm.us-east-1.elasticbeanstalk.com', 'localhost', '127.0.0.1' ]

</div>



