
# Watch Store ecommerce base on Flask

#### Create new venv on Windows
> py -3 -m venv venv
> venv\Scripts\activate
#### Install Flask
> pip install -r requirements.txt
- Add venv package to requirements.txt
> pip freeze > requirements.txt
#### Run Server
> flask --app server run
> flask --app server --debug run
#### Add packages into requirements.txt
> pip freeze > requirements.txt 


## References
[Flask](https://flask.palletsprojects.com/en/latest/)
[Flask-SQLAlchemy](https://flask-migrate.readthedocs.io/en/latest/)
[Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)

## Clear Cache
~~~
python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
python -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"


~~~