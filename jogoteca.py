from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
<<<<<<< HEAD
=======
from flask_bcrypt import Bcrypt
>>>>>>> melhoria-seguranca

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
<<<<<<< HEAD
=======
bcrypt = Bcrypt(app)
>>>>>>> melhoria-seguranca

from views_game import *
from views_user import *

if __name__ == '__main__':
    app.run(debug=True)