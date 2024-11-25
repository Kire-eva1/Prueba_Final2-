from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


@app.route('/resultado1', methods=['POST'])
def resultado1():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    tarros = int(request.form['tarros'])

    precio_tarro = 9000
    total_sin_descuento = tarros * precio_tarro

    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0

    total_con_descuento = total_sin_descuento * (1 - descuento)

    return f"Nombre: {nombre}, Total sin descuento: ${total_sin_descuento}, Total a pagar: ${total_con_descuento:.2f}"


@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


@app.route('/resultado2', methods=['POST'])
def resultado2():
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    if usuario in usuarios and usuarios[usuario] == contrasena:
        return f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
    else:
        return "Usuario o contraseña incorrectos."


if __name__ == '__main__':
    app.run(debug=True)