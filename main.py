import math
from flask import Flask, render_template, request
import forms

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST" :
        
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        
        if request.form.get("suma") :
            return "La suma de {} + {} = {}".format(num1, num2, str(int(num1) + int(num2)))
        
        elif request.form.get("resta") :
            return "La resta de {} - {} = {}".format(num1, num2, str(int(num1) - int(num2)))
        
        elif request.form.get("multiplicacion") :
            return "La multiplicación de {} x {} = {}".format(num1, num2, str(int(num1) * int(num2)))
        
        elif request.form.get("division") :
            return "La división de {} / {} = {}".format(num1, num2, str(int(num1) / int(num2)))

@app.route("/distancia", methods = ["GET", "POST"])
def distancia_dos_puntos():
    resultado = ""
    coordenada_x1 = float
    coordenada_x2 = float
    coordenada_y1 = float
    coordenada_y2 = float
    distancia_clase = forms.DistanciaForm(request.form)
    if request.method == 'POST' :
        coordenada_x1 = distancia_clase.coordenada_x1.data
        coordenada_x2 = distancia_clase.coordenada_x2.data
        coordenada_y1 = distancia_clase.coordenada_y1.data
        coordenada_y2 = distancia_clase.coordenada_y2.data
        
        resultado = math.sqrt((pow((coordenada_x2 - coordenada_x1), 2) + pow((coordenada_y2 - coordenada_y1), 2)))
    
    return render_template("distanciadospuntos.html", 
            form = distancia_clase, 
            coordenada_x1 = coordenada_x1,
            coordenada_x2 = coordenada_x2,
            coordenada_y1 = coordenada_y1,
            coordenada_y2 = coordenada_y2,
            resultado = resultado)

if __name__ ==  "__main__":
    app.run(debug=True)