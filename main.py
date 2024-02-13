import math
from flask import Flask, render_template, request
import forms
from ResistenciasCalculo import calcular_valores

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

@app.route("/resistenciasflask", methods=["GET", "POST"])
def CalculoResistencias():
    calct = forms.ResistenciaForm(request.form)

    primer_banda, segunda_banda, tercer_banda, radio_tol = "", "", "", None
    value, valor_maximo, valor_minimo, color1, color2, color3, color4 = 0, 0, 0, "", "", "", ""

    if request.method == "POST":
        
        primer_banda, segunda_banda, tercer_banda, radio_tol = request.form.get("primer_banda"), request.form.get("segunda_banda"), request.form.get("tercer_banda"), calct.radio_tol.data
        
        value, valor_maximo, valor_minimo, color1, color2, color3, color4 = calcular_valores(primer_banda, segunda_banda, tercer_banda, radio_tol)

    return render_template("resistenciasflask.html", 
                           form = calct, 
                           primer_banda = primer_banda, 
                           segunda_banda = segunda_banda, 
                           tercer_banda = tercer_banda,
                           value = value, 
                           valor_maximo = valor_maximo, 
                           valor_minimo = valor_minimo, 
                           color1 = color1, 
                           color2 = color2, 
                           color3 = color3, 
                           color4 = color4, 
                           radio_tol = radio_tol)

if __name__ ==  "__main__":
    app.run(debug=True)