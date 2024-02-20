import math
from flask import Flask, render_template, request
import forms
from io import open

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

## DICCIONARIO INGLÉS - ESPAÑOL
@app.route("/diccionario", methods=["GET", "POST"])
def diccionario():
    palabraIngles = ""
    palabraEspaniol = ""
    palabraABuscar = ""
    resultado = ""
    idioma = ""
    diccionario_class = forms.DiccionarioForm(request.form)
    
    if request.method == 'POST':
        if 'add_words' in request.form:
            if diccionario_class.palabraIngles.validate(diccionario_class) and diccionario_class.palabraEspaniol.validate(diccionario_class) :
                palabraIngles = diccionario_class.palabraIngles.data
                palabraEspaniol = diccionario_class.palabraEspaniol.data
                with open('diccionario.txt', 'a') as diccionario:
                    diccionario.write('{},{}\n'.format(palabraEspaniol, palabraIngles))
        elif 'translate_word' in request.form: 
            if diccionario_class.idioma.validate(diccionario_class):
                idioma = diccionario_class.idioma.data
                palabraABuscar = diccionario_class.palabraABuscar.data
                with open('diccionario.txt', 'r') as diccionario:
                    lineas = diccionario.readlines()            
                    for linea in lineas:
                        palabraEsp, palabraIng = linea.strip().split(',')
                        print(idioma)
                        if idioma == 'espaniol' and palabraABuscar.lower().strip() == palabraIng.lower().strip():
                            resultado = palabraEsp
                            break
                        elif idioma == 'ingles' and palabraABuscar.lower().strip() == palabraEsp.lower().strip():
                            resultado = palabraIng
                            break
                if resultado == "":
                    resultado = "Imposible_traducir"
            
    return render_template(
        "diccionario.html", 
        form=diccionario_class, 
        palabraIngles = palabraIngles,
        palabraEspaniol = palabraEspaniol,
        palabraABuscar = palabraABuscar,
        resultado = resultado)

## EXAMEN RESISTENCIA
@app.route("/resistencias", methods=["GET", "POST"])
def resistencia():
    banda1 = ""
    vBanda1 = 0
    banda2 = ""
    vBanda2 = 0
    banda3 = ""
    vBanda3 = 0
    tolerancia = ""
    vTolerancia = 0.0
    valor = 0.0
    valorMaximo = 0.0
    valorMinimo = 0.0
    resistencia_class = forms.ResitenciaForm(request.form)
    if request.method == "POST":
        banda1 = resistencia_class.primerBanda.data
        banda2 = resistencia_class.segundaBanda.data
        banda3 = resistencia_class.tercerBanda.data
        tolerancia = resistencia_class.tolerancia.data
        valorMaximo = resistencia_class.valorMaximo.data
        valorMinimo = resistencia_class.valorMinimo.data
        
        if banda1 == "negro":
            vBanda1 = "0"
        elif banda1 == "marron":
            vBanda1 = "1"
        elif banda1 == "rojo":
            vBanda1 = "2"
        elif banda1 == "naranja":
            vBanda1 = "3"
        elif banda1 == "amarillo":
            vBanda1 = "4"
        elif banda1 == "verde":
            vBanda1 = "5"
        elif banda1 == "azul":
            vBanda1 = "6"
        elif banda1 == "violeta":
            vBanda1 = "7"
        elif banda1 == "gris":
            vBanda1 = "8"
        elif banda1 == "blanco":
            vBanda1 = "9"
            
        if banda2 == "negro":
            vBanda2 = "0"
        elif banda2 == "marron":
            vBanda2 = "1"
        elif banda2 == "rojo":
            vBanda2 = "2"
        elif banda2 == "naranja":
            vBanda2 = "3"
        elif banda2 == "amarillo":
            vBanda2 = "4"
        elif banda2 == "verde":
            vBanda2 = "5"
        elif banda2 == "azul":
            vBanda2 = "6"
        elif banda2 == "violeta":
            vBanda2 = "7"
        elif banda2 == "gris":
            vBanda2 = "8"
        elif banda2 == "blanco":
            vBanda2 = "9"
            
        if banda3 == "negro":
            vBanda3 = "1"
        elif banda3 == "marron":
            vBanda3 = "10"
        elif banda3 == "rojo":
            vBanda3 = "100"
        elif banda3 == "naranja":
            vBanda3 = "1000"
        elif banda3 == "amarillo":
            vBanda3 = "10000"
        elif banda3 == "verde":
            vBanda3 = "100000"
        elif banda3 == "azul":
            vBanda3 = "1000000"
        elif banda3 == "violeta":
            vBanda3 = "10000000"
        elif banda3 == "gris":
            vBanda3 = "100000000"
        elif banda3 == "blanco":
            vBanda3 = "1000000000"
            
        
        if tolerancia == "dorado":
            vTolerancia = 0.05
        elif tolerancia == "plateado":
            vTolerancia = 0.1
            
        valor = int(vBanda1 + vBanda2) * int(vBanda3)
        valorMinimo = valor - (valor * vTolerancia)
        valorMaximo = valor + (valor * vTolerancia) 
        
        print("multiplicador: {}".format(banda3))
    return render_template(
        "resistencia.html",
        form = resistencia_class,
        primerBanda = banda1,
        segundaBanda = banda2,
        tercerBanda = banda3,
        tolerancia = tolerancia,
        valor = valor,
        valorMinimo = valorMinimo,
        valorMaximo = valorMaximo
    )

## Distancia entre dos puntos
@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    coord_x1 = ""
    coord_x2 = ""
    coord_y1 = ""
    coord_y2 = ""
    resultado = ""
    distancia_class = forms.DistanciaForm(request.form)
    if request.method == "POST":
        coord_x1 = distancia_class.x1.data
        coord_x2 = distancia_class.x2.data
        coord_y1 = distancia_class.y1.data
        coord_y2 = distancia_class.y2.data
        resultado = math.sqrt((pow((coord_x2 - coord_x1), 2) + pow((coord_y2 - coord_y1), 2)))
        
        print('x1: {}, y1: {}, x2: {}, y2: {}, resultado = {}'.format(coord_x1, coord_y1, coord_x2, coord_y2, resultado))
        
    return render_template(
        "distancia.html", 
        form = distancia_class, 
        x1 = coord_x1,
        x2 = coord_x2,
        y1 = coord_y1,
        y2 = coord_y2,
        resultado = resultado
    )

@app.route("/operaciones")
def operaciones():
    return render_template("operaciones.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado(): 
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        operacion = request.form.get("operacion")
        
        if operacion == "suma":
            return "La suma de {} + {} = {}".format(n1, n2, str(int(n1) + int(n2)))
        elif operacion == "resta":
            return "La resta de {} - {} = {}".format(n1, n2, str(int(n1) - int(n2)))
        elif operacion == "multiplicacion":
            return "La multiplicación de {} x {} = {}".format(n1, n2, str(int(n1) * int(n2)))
        elif operacion == "division":
            return "La division de {} / {} = {}".format(n1, n2, str(int(n1) / int(n2)))
        
if __name__ == "__main__":
    app.run(debug=True)