from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("operaciones.html")

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