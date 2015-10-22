# Getting Started with Django

Django is an open source, Python based web application framework. The technology we've studied in class that it resembles the most is Ruby on Rails.  Like Rails, it also follows the MVC pattern and is a means of creating clean code with resusable components.  Django was first released in 2005 and is currently maintained by the Django Software Foundation.

**1. Install Python**

To see if you already have Python 3 (best option) installed on your computer, type the following:

    $ python3 --version

If not,

    $ brew install python3


 You can now type python3 at the command line to enter the python console and write/run python code

**2. Install Pip**
   * should be included in Python 3

    $ sudo easy_install pip

**3. Install Django**

    $ pip install django


**4. To create and enter a virtual environment for your project, type the following in the directory you plan to place your project in:**

    $ python3 -m venv myvenv

    $ source myvenv/bin/activate

* You will know it's successful if the command line prompt now has (myvenv) in front of it

**5. To start a new project, type the following:**

(myvenv) ~/djangogirls$ django-admin startproject mysite .

**6. Create a separate folder in the main project directory for models, views, url paths, etc:**

* in the case of a blog application, we create a blog folder

    (myvenv) ~/projectdirectory python manage.py startapp blog

The default database for Django projects is sqlite3 (you can see this in the mysite/settings.py file).

To create the actual database, type the following:

    (myvenv) ~/projectdirectory python manage.py migrate

To add a model to the database, type the following:

    (myvenv) ~/projectdirectory  python manage.py makemigrations blog

* this lets django know you created a model

    (myvenv) ~/projectdirectory  python manage.py migrate blog

* this applies the model to database

To run the server, type the following:

    (myvenv) ~/projectdirectory python3 manage.py runserver to run server

* the server is http://127.0.0.1:8000/

When the webpage gets a request, the 'urlresolver' figures out which view to render (the urls.py file contains the patterns urlresolver uses).

Django uses something called a 'superuser' as a way of allowing a user to create an account and have access to add, edit, update, and delete, and view certain items.  To create an account for a new superuser, type the following:

    (myvenv) ~/projectdirectory python manage.py createsuperuser
