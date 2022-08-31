from flask import Flask
app = Flask(__name__)

#1. Localhost:5000/: haz que diga "¡Hola Mundo!"
@app.route('/')
def hola_mundo():
    print("Hola")
    return '¡Hola Mundo!'

#2. Localhost:5000/dojo: haz que diga "¡Dojo!"
@app.route('/dojo')
def aisha():
    print("dojo")
    return '¡Dojo!'

#3. Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos:
# localhost:5000/say/flask: haz que diga "¡Hola, Flask!"
# localhost:5000/say/ Michael: haz que diga "¡Hola, Michael!
#localhost:5000/say/john: haz que diga "¡Hola, John!"
@app.route('/say/<name>')
def hola(name):
    print(name)
    return f"¡Hola, {name}!"

# 4 Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos
# (PISTA: int() puede ser útil Por ejemplo, int('35*) devuelve 35):
#• localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
#• localhost:5000/repeat/80/bye: haz que diga 'adiós' 80 veces
#• localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces 0
@app.route('/repeat/<int:num>/<string:name>')
def module_coding_dojo(num,name):
    response = ""
    for x in range(0,num):
        response = response + "<h1>" + name + "<h1>"
    print(response)
    return response

# BONUS SENSE: Asegúrate de que si el usuario escribe cualquier ruta distinta a las
# especificadas, reciba un mensaje de error que diga ¡Lo siento! No hay respuesta.
# Inténtalo otra vez.".

@app.route('/ ', defaults={'path': ''})
@app.route('/<path:path>')
def cath_all(path):
    return "<h2>Lo siento no hay respuesta, Intentalo otra vez.</h2>"


if __name__=="__main__":
    app.run(debug=True)