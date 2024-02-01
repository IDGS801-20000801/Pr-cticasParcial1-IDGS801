from wtforms import Form
from wtforms import IntegerField

class DistanciaForm(Form):
    coordenada_x1 = IntegerField("X1")
    coordenada_y1 = IntegerField("Y1")
    
    coordenada_x2 = IntegerField("X2")
    coordenada_y2 = IntegerField("Y2")