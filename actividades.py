"""
    El usuario escribe un número entero positivo que corresponde al número de unidades del producto a comprar
    y otro que corresponde al precio unitario de ese producto.
    Con esos dos valores se deben ejecutar las operaciones necesarias para realizar el cálculo del monto total a pagar por el cliente,
    que se desglosa como sub-total, descuento y total a pagar.
    Para calcular el descuento que se aplica se toma como base lo siguiente:
    • Si el cliente compra más de 100 unidades se aplica un descuento del 40%.
    • Si el cliente compra entre 25 y 100 unidades se aplica un descuento de 20%.
    • Si el cliente compra entre 10 y 24 unidades se aplica un descuento del 10%.
    • Si el cliente compra menos de 10 unidades no se aplica ningún descuento.
:return:
"""

import os
import sqlite3


def actividad1():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Cálculo de Compra</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f9f9f9;
                padding: 20px;
            }
            .container {
                background: #fff;
                border: 1px solid #ddd;
                padding: 20px;
                max-width: 400px;
                margin: 0 auto;
                box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
            }
            input, button {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
            }
            .resultado {
                background: #e8f5e9;
                border: 1px solid #a5d6a7;
                padding: 10px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Cálculo de Compra 1</h2>
            <label for="unidades">Número de unidades:</label>
            <input type="number" id="unidades" min="1" placeholder="Ingrese número de unidades">

            <label for="precio">Precio unitario:</label>
            <input type="number" id="precio" min="0" step="0.01" placeholder="Ingrese precio unitario">

            <button onclick="calcularCompra()">Calcular</button>

            <div id="resultado" class="resultado"></div>
        </div>

        <script>
            function calcularCompra() {
                // Obtener los valores ingresados por el usuario
                var unidades = parseInt(document.getElementById('unidades').value);
                var precio = parseFloat(document.getElementById('precio').value);

                // Validación de los datos ingresados
                if (isNaN(unidades) || isNaN(precio) || unidades <= 0 || precio < 0) {
                    alert('Por favor, ingrese valores válidos.');
                    return;
                }

                // Cálculo del sub-total: número de unidades * precio unitario
                var subtotal = unidades * precio;

                // Determinar el porcentaje de descuento según el número de unidades
                var porcentajeDescuento = 0;
                if (unidades > 100) {
                    porcentajeDescuento = 40;
                } else if (unidades >= 25 && unidades <= 100) {
                    porcentajeDescuento = 20;
                } else if (unidades >= 10 && unidades <= 24) {
                    porcentajeDescuento = 10;
                } else {
                    porcentajeDescuento = 0;
                }

                // Cálculo del descuento en pesos
                var descuento = subtotal * (porcentajeDescuento / 100);

                // Cálculo del total a pagar
                var total = subtotal - descuento;

                // Mostrar los resultados en pantalla
                var resultadoDiv = document.getElementById('resultado');
                resultadoDiv.innerHTML = '<p><strong>Sub-total:</strong> $' + subtotal.toFixed(2) + '</p>' +
                                          '<p><strong>Descuento (' + porcentajeDescuento + '%):</strong> $' + descuento.toFixed(2) + '</p>' +
                                          '<p><strong>Total a pagar:</strong> $' + total.toFixed(2) + '</p>';
            }
        </script>
    </body>
    </html>
    """
    return html_content


def actividad2():
    """ Uso de templates """
    return "actividad3.html"


def actividad3(unidades, precio):
    # Validación de los datos de entrada
    if unidades <= 0 or precio < 0:
        return {"error": "Valores inválidos, debe ingresar números positivos."}

    # Cálculo del sub-total
    subtotal = unidades * precio

    # Determinar el porcentaje de descuento
    if unidades > 100:
        porcentaje_descuento = 40
    elif unidades >= 25:
        porcentaje_descuento = 20
    elif unidades >= 10:
        porcentaje_descuento = 10
    else:
        porcentaje_descuento = 0

    # Cálculo del descuento
    descuento = subtotal * (porcentaje_descuento / 100)

    # Total a pagar
    total = subtotal - descuento

    # Retorno de resultados en un diccionario
    return {
        "sub_total": round(subtotal, 2),
        "descuento_aplicado": f"{porcentaje_descuento}%",
        "monto_descuento": round(descuento, 2),
        "total_a_pagar": round(total, 2)
    }

class Actividad4:

    def calcular_descuento(self, unidades, precio):
        # Validación de los datos de entrada
        if unidades <= 0 or precio < 0:
            return {"error": "Valores inválidos, debe ingresar números positivos."}

        # Cálculo del sub-total
        subtotal = unidades * precio

        # Determinar el porcentaje de descuento
        if unidades > 100:
            porcentaje_descuento = 40
        elif unidades >= 25:
            porcentaje_descuento = 20
        elif unidades >= 10:
            porcentaje_descuento = 10
        else:
            porcentaje_descuento = 0

        # Cálculo del descuento
        descuento = subtotal * (porcentaje_descuento / 100)

        # Total a pagar
        total = subtotal - descuento

        # Retorno de resultados en un diccionario
        return {
            "sub_total": round(subtotal, 2),
            "descuento_aplicado": f"{porcentaje_descuento}%",
            "monto_descuento": round(descuento, 2),
            "total_a_pagar": round(total, 2)
        }

class actividad5:
    """ Modelo para la base de datos producto utilizado en la activiad 5 """

    schema = "CREATE TABLE IF NOT EXISTS producto (id INTEGER PRIMARY KEY, nombre TEXT, precio FLOAT)"
    database = "my_db_act5.sqlite3"
    db = None

    def start(self):
        try:
            if not os.path.exists(self.database):
                self.create_db()
            else:
                # se conecta a la db y la asigna al parametro
                self.db = sqlite3.connect(self.database)
        except sqlite3.Error as e:
            raise RuntimeError(f"ERROR: {e}")

    def create_db(self):
        # crea la db si no existe
        db = sqlite3.connect(self.database)
        cursor = db.cursor()
        cursor.execute(self.schema)
        db.commit()
        db.close()
        self.db = db

    def insert_init(self):
        # inserta productos ejemplo
        self.insert(name="p1", price=10.1)
        self.insert(name="p2", price=20.0)


    def execute(self, command):
        try:
            cursor = self.db.cursor()
            cursor.execute(command)
            self.db.commit()
            return True
        except sqlite3.Error as e:
            print(f'{e.sqlite_errorcode}: {e.sqlite_errorname}')
            return False

    def list(self):
        productos_l = []

        try:
            cursor = self.db.cursor()
            cursor.execute('SELECT * FROM producto')
            productos = cursor.fetchall()

            print(productos)

            for producto in productos:
                productos_l.append({
                    'id': producto[0],
                    'nombre': producto[1],
                    'precio': producto[2]
                })

            return productos_l

        except sqlite3.Error as e:
            return {'error': f'code {e.sqlite_errorcode}: {e.sqlite_errorname}'}


    def get_by_id(self, id):

        if id is None:
            return {'error': f'procurar id es necesario'}

        try:
            cursor = self.db.cursor()
            cursor.execute(f'SELECT * FROM producto WHERE id = {id}')
            producto = cursor.fetchone()

            print(producto)

            if producto:
                return {
                    'id': producto[0],
                    'nombre': producto[1],
                    'precio': producto[2]
                }
            else:
                return {'error': "producto no encontrado"}

        except sqlite3.Error as e:
            return {'error': f'code {e.sqlite_errorcode}: {e.sqlite_errorname}'}

    def insert(self, **kwargs):
        name = kwargs.get("name", None)
        price = kwargs.get("price", None)

        if not name or not price:
            return "nombre y precio son necesarios"

        result = self.execute(f'INSERT INTO producto (nombre, precio) VALUES ("{name}",{price})')
        return result

    def delete(self, id):

        if not id:
            return "id son necesarios"

        result = self.execute(f'DELETE from producto WHERE id = {id}')
        return result