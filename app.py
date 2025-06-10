from flask import Flask, render_template_string, render_template, request, jsonify
from actividades import actividad1, actividad2, actividad3, Actividad4, actividad5

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Starting Flask...")
    return "<p>Hello, World!</p>"


@app.route("/act1")
def mostrar_actividad1():
    """ Renderizado de cadena de texto"""

    # llamamos a la funcion actividad1 y la renderiza
    return render_template_string(actividad1())


@app.route("/act2")
def mostrando_actividad2():
    """ Renderizado de HTML usando templates"""

    return render_template(actividad2())


@app.route("/act3",  methods=['GET'])
def mostrar_actividad3():
    """ Respuesta JSON API REST"""

    # Obtener parámetros desde la URL (query params)
    unidades = request.args.get('unidades', 1, type=int)
    precio = request.args.get('precio', 0, type=float)

    # Llamamos a la función y obtenemos el resultado
    resultado = actividad3(unidades, precio)

    # Retornamos el resultado en formato JSON
    return jsonify(resultado)


@app.route("/act4",  methods=['GET', 'POST'])
def mostrar_actividad4():
    """ USANDO POO y REQUEST"""

    act4 = Actividad4()

    if request.method == "POST":
        unidades = request.form.get("unidades", type=int)
        precio = request.form.get("precio", type=float)

        resultado = act4.calcular_descuento(unidades, precio)
        return render_template("actividad4_resultado.html", resultado=resultado) # jinja2

    return render_template("actividad4_index.html")


# ACTIVIDAD 5 API
@app.route("/producto/",  methods=['GET'])
def act5_list():
    try:
        mprod = actividad5()
        mprod.start()
        result = mprod.list()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"{e}"})

@app.route("/producto/<int:pid>",  methods=['GET'])
def act5_get(pid):
    try:
        mprod = actividad5()
        mprod.start()
        result = mprod.get_by_id(pid)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"{e}"})

@app.route("/producto/agregar/",  methods=['POST'])
def act5_insert():
    data = request.get_json()
    name = data.get('nombre')
    price = data.get('precio')

    if not name:
        return jsonify({'error': 'nombre requerido'})
    if not price:
        return  jsonify({'error': 'precio requerido'})

    try:
        mprod = actividad5()
        mprod.start()
        result = mprod.insert(name=name, price=price)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"{e}"})

@app.route("/producto/borrar/<int:id>",  methods=['GET'])
def act5_delete(id):
    try:
        mprod = actividad5()
        mprod.start()
        result = mprod.delete(id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"{e}"})


# ACTIVIDAD 6 app

@app.route("/act6",  methods=['GET'])
def mostrar_actividad6():
    """ Simple CRUD , single page  """
    return render_template("actividad6_index.html")

@app.route("/act6/list",  methods=['GET'])
def list_actividad6():
    """ get list using partial template  """
    try:
        mprod = actividad5()
        mprod.start()
        productos = mprod.list()
    except Exception as e:
        return [{"error": f"{e}"}]
    return render_template("actividad6_table.html", productos=productos)

"""""
Flask es un microframework de Python que permite desarrollar aplicaciones web de manera rápida y sencilla. 
Sus principales funcionalidades incluyen:

1. Rutas y Vistas
Definir rutas (@app.route('/')) para diferentes páginas web.

Enviar respuestas en formato HTML, JSON, o texto plano.

2. Renderización de Plantillas
Utilizar render_template('archivo.html') para cargar HTML desde la carpeta templates.

Integración con Jinja2 para plantillas dinámicas ({{ variable }}).

3. Manejo de Formularios y Datos
Capturar datos de formularios con request.form.get('campo').

Obtener parámetros de la URL con request.args.get('parametro').

4. Manejo de Sesiones y Cookies
Guardar información temporal de usuario con session['clave'] = valor.

Trabajar con cookies utilizando response.set_cookie('nombre', valor).

5. API REST y Respuestas JSON
Crear APIs con jsonify({'mensaje': 'Hola'}).

Soporte para métodos GET, POST, PUT, DELETE.

6. Manejo de Archivos Estáticos
Servir CSS, JS e imágenes desde la carpeta static.

Acceder a archivos estáticos con url_for('static', filename='archivo.css').

7. Blueprints (Modularización)
Separar rutas en módulos (Blueprint) para proyectos grandes.

8. Extensiones para Bases de Datos
Integración con SQLAlchemy para bases de datos.

Conexión con SQLite, MySQL, PostgreSQL.

9. Middleware y Seguridad
Implementación de autenticación y autorización.

Protección contra ataques CSRF y XSS.

10. Pruebas y Debugging
Modo de depuración con app.run(debug=True).

"""