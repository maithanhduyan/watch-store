
# Watch Store ecommerce base on Flask

#### Watch Store Galery
![Home Page](https://github.com/maithanhduyan/watch-store/blob/master/shop/static/images/screencapture.png?raw=true)
#### Create new venv on Windows
> py -3 -m venv venv
> venv\Scripts\activate
#### Install Flask
> pip install -r requirements.txt
- Add venv package to requirements.txt
> pip freeze > requirements.txt
#### Run Server
> flask --app shop run
> flask --app shop --debug run
#### Add packages into requirements.txt
> pip freeze > requirements.txt 


## References
[Flask](https://flask.palletsprojects.com/en/latest/)
[Flask-SQLAlchemy](https://flask-migrate.readthedocs.io/en/latest/)
[Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)


[Icons8](https://icons8.com/)

## Clear Cache
~~~
python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
python -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"


~~~
