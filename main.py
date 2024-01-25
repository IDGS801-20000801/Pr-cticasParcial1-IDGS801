from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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

if __name__ ==  "__main__":
    app.run(debug=True)