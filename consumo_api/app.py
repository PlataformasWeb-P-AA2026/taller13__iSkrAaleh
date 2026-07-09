from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import json

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'una-clave-secreta-000001'

token = '86de50ad0b8a39b3ecec46bc2d89b4a438db29e7'
headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

@app.route("/")
def hello_world():
    return "<p>Hola mundo desde Flask</p>"

@app.route("/los/edificios")
def los_edificios():
    """
    """
    r = requests.get("http://localhost:8000/api/edificios/", headers=headers)
    print("---------------------")
    print(r.content)
    print("---------------------")
    edificios = json.loads(r.content)['results']

    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


def obtener_edificio(url):
    """
    http://127.0.0.1:8000/api/edificios/1/
    """
    r = requests.get(url, headers=headers)
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio


@app.route("/los/departamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://localhost:8000/api/departamentos/", headers=headers)
    departamentos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']
    
    datos = []
    for d in departamentos:
        datos.append({
            'nombre_propietario': d['nombre_propietario'],
            'costo': d['costo'],
            'numero_cuartos': d['numero_cuartos'],
            'edificio': obtener_edificio(d['edificio'])
        })
        
    return render_template("losdepartamentos.html", departamentos=datos,
    numero_departamentos=numero_departamentos)


@app.route("/crear/edificio", methods=['GET', 'POST'])
def agregar_edificio():
    """
    """
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        tipo = request.form['tipo']

        # Datos a enviar a la API de Django
        edificio_data = {
            'nombre': nombre,
            'direccion': direccion,
            'ciudad': ciudad,
            'tipo': tipo
        }

        # Realizar la petición POST a la API de Django
        r = requests.post("http://localhost:8000/api/edificios/",
                              json=edificio_data,
                              headers=headers)

        print(f"Status Code (Crear Edificio): {r.status_code}")
        nuevo_edificio = json.loads(r.content)
        flash(f"Edificio '{nuevo_edificio['nombre']}' creado exitosamente!", 'success')
        return redirect(url_for('los_edificios'))

    return render_template("crear_edificio.html")


@app.route("/crear/departamento", methods=['GET', 'POST'])
def crear_departamento():
    """
    """
    edificios_disponibles = []

    r_edificios = requests.get("http://localhost:8000/api/edificios/", headers=headers)
    edificios_disponibles = json.loads(r_edificios.content)['results']

    if request.method == 'POST':
        nombre_propietario = request.form['nombre_propietario']
        costo = request.form['costo']
        numero_cuartos = request.form['numero_cuartos']
        edificio_url = request.form['edificio']

        departamento_data = {
            'nombre_propietario': nombre_propietario,
            'costo': costo,
            'numero_cuartos': numero_cuartos,
            'edificio': edificio_url
        }

        r = requests.post("http://localhost:8000/api/departamentos/",
                              json=departamento_data,
                              headers=headers)

        print(f"Status Code (Crear Departamento): {r.status_code}")

        nuevo_departamento = json.loads(r.content)
        flash(f"Departamento de '{nuevo_departamento['nombre_propietario']}' creado exitosamente!", 'success')
        return redirect(url_for('los_departamentos'))

    return render_template("crear_departamento.html",
                           edificios=edificios_disponibles,
                           )

if __name__ == "__main__":
    app.run(debug=True)
