import math
from flask import Flask, render_template, request
import forms

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

## EXAMEN RESISTENCIA
@app.route("/resistencias", methods=["GET", "POST"])
def resistencia():
    banda1 = ""
    vBanda1 = 0
    cBanda1 = ""
    banda2 = ""
    vBanda2 = 0
    cBanda2 = ""
    banda3 = ""
    vBanda3 = 0
    cBanda3 = ""
    tolerancia = ""
    vTolerancia = 0.0
    cTolerancia = ""
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
            cBanda1 = "#000000"
        elif banda1 == "marron":
            vBanda1 = "1"
            cBanda1 = "#593B19"
        elif banda1 == "rojo":
            vBanda1 = "2"
            cBanda1 = "#9F1307"
        elif banda1 == "naranja":
            vBanda1 = "3"
            cBanda1 = "#FF9118"
        elif banda1 == "amarillo":
            vBanda1 = "4"
            cBanda1 = "#FFF800"
        elif banda1 == "verde":
            vBanda1 = "5"
            cBanda1 = "#00B54C"
        elif banda1 == "azul":
            vBanda1 = "6"
            cBanda1 = "#0069B5"
        elif banda1 == "violeta":
            vBanda1 = "7"
            cBanda1 = "#8F00B5"
        elif banda1 == "gris":
            vBanda1 = "8"
            cBanda1 = "#8B8B8B"
        elif banda1 == "blanco":
            vBanda1 = "9"
            cBanda1 = "#FFFFFF"
            
        if banda2 == "negro":
            vBanda2 = "0"
            cBanda2 = "#000000"
        elif banda2 == "marron":
            vBanda2 = "1"
            cBanda2 = "#593B19"
        elif banda2 == "rojo":
            vBanda2 = "2"
            cBanda2 = "#9F1307"
        elif banda2 == "naranja":
            vBanda2 = "3"
            cBanda2 = "#FF9118"
        elif banda2 == "amarillo":
            vBanda2 = "4"
            cBanda2 = "#FFF800"
        elif banda2 == "verde":
            vBanda2 = "5"
            cBanda2 = "#00B54C"
        elif banda2 == "azul":
            vBanda2 = "6"
            cBanda2 = "#0069B5"
        elif banda2 == "violeta":
            vBanda2 = "7"
            cBanda2 = "#8F00B5"
        elif banda2 == "gris":
            vBanda2 = "8"
            cBanda2 = "#8B8B8B"
        elif banda2 == "blanco":
            vBanda2 = "9"
            cBanda2 = "#FFFFFF"
            
        if banda3 == "negro":
            vBanda3 = "0"
            cBanda3 = "#000000"
        elif banda3 == "marron":
            vBanda3 = "10"
            cBanda3 = "#593B19"
        elif banda3 == "rojo":
            vBanda3 = "10"
            cBanda3 = "#9F1307"
        elif banda3 == "naranja":
            vBanda3 = "100"
            cBanda3 = "#FF9118"
        elif banda3 == "amarillo":
            vBanda3 = "1000"
            cBanda3 = "#FFF800"
        elif banda3 == "verde":
            vBanda3 = "10000"
            cBanda3 = "#00B54C"
        elif banda3 == "azul":
            vBanda3 = "6"
            cBanda3 = "#0069B5"
        elif banda3 == "violeta":
            vBanda3 = "7"
            cBanda3 = "#8F00B5"
        elif banda3 == "gris":
            vBanda3 = "8"
            cBanda3 = "#8B8B8B"
        elif banda3 == "blanco":
            vBanda3 = "9"
            cBanda3 = "#FFFFFF"
            
        
        if tolerancia == "dorado":
            vTolerancia = 0.05
            cTolerancia = "#CE9E03"
        elif tolerancia == "plateado":
            vTolerancia = 0.1
            cTolerancia = "#DAE7E5"
            
        valor = int(vBanda1 + vBanda2) * int(vBanda3)
        valorMinimo = valor - (valor * vTolerancia)
        valorMaximo = valor + (valor * vTolerancia) 
        
        print("multiplicador: {}".format(banda3))
    return render_template(
        "resistencia.html",
        form = resistencia_class,
        primerBanda = banda1,
        colorPrimerBanda = cBanda1,
        segundaBanda = banda2,
        colorSegundaBanda = cBanda2,
        tercerBanda = banda3,
        colorMultiplicador = cBanda3,
        tolerancia = tolerancia,
        colorTolerancia = cTolerancia,
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