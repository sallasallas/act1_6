# NOT USED

import os

from flask import Flask, g
import sqlite3

app = Flask(__name__)


class sqlite_db:

    database = None
    schema = None

    def __init__(self, database, schema):
        """ Constructor """
        self.database = database
        self.schema = schema
        self.validate()
        self.create_db()

    def validate(self):
        if self.database is None:
            raise RuntimeError("Porfavor especifique la base datos")
        if self.schema is None:
            raise RuntimeError("Porfavor especifique cual esquema de la base de datos")

    def get_db(self):
        """ Se conecta y/o crea la bd y luego devuelve el apuntador """
        db = getattr(g, '_database', None) # verifica si la coneccion es
        if self.database == "":
            self.create_db()
        if db is None:
            db = g._database = sqlite3.connect(self.database)
        return db

    def create_db(self):
        """  Crea la bd si no existe """
        if not os.path.exists(self.database):
            db = sqlite3.connect(self.database)
            cursor = db.cursor()
            cursor.execute(self.init_db_command)
            db.commit()
            db.close()

    def destroy_db(self):
        """ Elimina el archivo de la base de datos """
        if os.path.exists(self.database):
            os.remove(self.database)



class modelo_producto:
    """ Modelo de la bd producto """

    name = "producto"
    schema = "CREATE TABLE IF NOT EXISTS producto (id INTEGER PRIMARY KEY, nombre TEXT, precio FLOAT)"

    def get(self):
        return 'SELECT * FROM producto'

    def get_by(self, **kwargs):
        if not kwargs.get("id", None) is None:
            id = kwargs.get("id")
            return f'SELECT FROM producto WHERE id = {id}'
        if not kwargs.get("nombre", None) is None:
            name = kwargs.get("nombre")
            return f'SELECT FROM producto WHERE name = {name}'
        return False

    def insert(self, **kwargs):
        if not kwargs.get("id", None) is None:
            id = kwargs.get("id")
            return f'INSERT INTO producto (name) VALUES ({id})'
        if not kwargs.get("nombre", None) is None:
            name = kwargs.get("nombre")
            return f'INSERT INTO producto (name) VALUES ({name})'
        return False

    def delete(self, id):
        return f'DELETE from prodcuto WHERE id = {id}'