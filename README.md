# Installation

`pip3 install -r requirements.txt`

# Running

MAC: `FLASK_APP=index.py flask run`
WINDOWS: `python index.py`

# Heroku

1. Push to master: `git push heroku master`
2. Scale dynos: `heroku ps:scale web=1`