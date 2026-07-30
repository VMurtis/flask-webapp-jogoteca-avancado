SECRET_KEY = 'flask'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'mycode',
        servidor = 'localhost',
        database = 'jogoteca'
    )