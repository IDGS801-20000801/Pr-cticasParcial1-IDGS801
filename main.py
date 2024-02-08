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
    
@app.route("/resistenciasflask", methods = ["GET", "POST"])
def calcularResistencia():
    color_1 = str
    color_2 = str
    color_3 = str
    tolerancia = str
    valor = str
    valormaximo = str
    valorminimo = str
    banda_concatenada = str
    
    if request.form.get("banda1") == "negro":
        color_1 = "0"
    elif request.form.get("banda1") == "cafe":
        color_1 = "1"
    elif request.form.get("banda1") == "rojo":
        color_1 = "2"
    elif request.form.get("banda1") == "naranja":
        color_1 = "3"
    elif request.form.get("banda1") == "amarillo":
        color_1 = "4"
    elif request.form.get("banda1") == "verde":
        color_1 = "5"
    elif request.form.get("banda1") == "azul":
        color_1 = "6"
    elif request.form.get("banda1") == "violeta":
        color_1 = "7"
    elif request.form.get("banda1") == "gris":
        color_1 = "8"
    elif request.form.get("banda1") == "blanco":
        color_1 = "9"
    
    if request.form.get("banda2") == "negro":
        color_2 = "0"
    elif request.form.get("banda2") == "cafe":
        color_2 = "1"
    elif request.form.get("banda2") == "rojo":
        color_2 = "2"
    elif request.form.get("banda2") == "naranja":
        color_2 = "3"
    elif request.form.get("banda2") == "amarillo":
        color_2 = "4"
    elif request.form.get("banda2") == "verde":
        color_2 = "5"
    elif request.form.get("banda2") == "azul":
        color_2 = "6"
    elif request.form.get("banda2") == "violeta":
        color_2 = "7"
    elif request.form.get("banda2") == "gris":
        color_2 = "8"
    elif request.form.get("banda2") == "blanco":
        color_2 = "9"
        
    if request.form.get("banda3") == "negro":
        color_3 = "1"
    elif request.form.get("banda3") == "cafe":
        color_3 = "10"
    elif request.form.get("banda3") == "rojo":
        color_3 = "100"
    elif request.form.get("banda3") == "naranja":
        color_3 = "1000"
    elif request.form.get("banda3") == "amarillo":
        color_3 = "10000"
    elif request.form.get("banda3") == "verde":
        color_3 = "100000"
    elif request.form.get("banda3") == "azul":
        color_3 = "1000000"
    elif request.form.get("banda3") == "violeta":
        color_3 = "10000000"
    elif request.form.get("banda3") == "gris":
        color_3 = "100000000"
    elif request.form.get("banda3") == "blanco":
        color_3 = "1000000000"
            
    if request.form.get("dorado"):
        tolerancia = "0.05"
    elif request.form.get("plata"):
        tolerancia = "0.10"
    
    if request.method == 'POST':
        return render_template("resistenciasflask.html", 
                           color_1 = color_1, color_2 = color_2, 
                           color_3 = color_3, valor = valor)

if __name__ ==  "__main__":
    app.run(debug=True)