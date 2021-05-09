Install docker
--------------
`sudo snap install docker`


Setup environment
-----------------
Copy the file .env.example to a new .env file
Make the changes in that file to setup a local environment.

Local environment setup
-----------------------
`cd matrimony`

`python manage.py migrate`

Docker environment setup
------------------------
`docker-compose build`
`docker-compose up`

Migrations and test (New tab)
------------------------------
`docker-compose run django_rest python manage.py makemigrations`

`docker-compose run django_rest python manage.py migrate`

`docker-compose run django_rest python manage.py test`
