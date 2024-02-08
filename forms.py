from wtforms import Form
from wtforms import IntegerField, StringField

class DistanciaForm(Form):
    coordenada_x1 = IntegerField("X1")
    coordenada_y1 = IntegerField("Y1")
    
    coordenada_x2 = IntegerField("X2")
    coordenada_y2 = IntegerField("Y2")
    
class ResistenciaForm(Form):
    primer_banda = StringField("1ra. Banda")
    segunda_banda = StringField("2da. Banda")
    tercer_banda = StringField("3ra. Banda (Multiplicador)")