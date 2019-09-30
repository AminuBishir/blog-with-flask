# blog-with-flask
A personal blog web app developed using python's Flask framework. This project is great start for anyone that want to develop a blog web app using Flask framework. It's also a great resource for developers that want explore things like flask framework, Postgresql, SQLAlchemy orm, flask-login etc.
# Requirements
To successfully run this web app, one needs to fulfill the following requirements:
1. Have postgresql db installed and create (or import) the database named ```sadarwa```
2. python version: 3.x
3. Flask (if you don't have one installed): ```$ pip install flask```
4. SQLAlchemy (a python based Object Relational Model -ORM): ```$ pip install -U Flask-SQLAlchemy```
5. flask-login (for handling login in and out): ```$ pip install Flask-Login```
6. WTForm (for generating and validating forms): ```$ pip install wtform```
7. Jinja2 (in case in if it is not installed): ```$ pip install jinja2```
8. Bootstrap 4: Download and put it in the /static folder, note that the name of the bootsrap folder should be ```bootstrap``` as specified in the <head> tag used (but you can still change it if you so wish)

To run the web app, navigate the project folder in your shell and then run the web app by typing ```python main.py```

# API Endpoionts
To show how easy it is to make APIs using flask sqlalchemy, we provide one api end point (accessible vai ```/comments/<int:user_id>``` that will return all the comments made a user in form json.
