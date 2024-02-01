import math
from flask import Flask, render_template, request
import forms

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")


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