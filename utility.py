import requests

from actividades import actividad5


def act5_insert_product(url):
    #'http://127.0.0.1:5000/producto/agregar'
    data = {
        "nombre": "p1515",
        "precio": 15.15
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("AGREGADO: ", response.json())
    else:
        print('Error:', response.status_code, response.text)


def act5_start_db():
    try:
        mprod = actividad5()
        mprod.start()
        return "db created"
    except Exception as e:
        return {"error": f"{e}"}

def act5_start_insert():
    try:
        mprod = actividad5()
        mprod.start()
        mprod.insert_init()
        return "init inserted"
    except Exception as e:
        return {"error": f"{e}"}
