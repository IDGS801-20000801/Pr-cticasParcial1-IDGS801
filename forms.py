from wtforms import Form
from wtforms import IntegerField, SelectField, RadioField

class DistanciaForm(Form):
    coordenada_x1 = IntegerField("X1")
    coordenada_y1 = IntegerField("Y1")
    
    coordenada_x2 = IntegerField("X2")
    coordenada_y2 = IntegerField("Y2")
    
class ResistenciaForm(Form):
    primer_banda = SelectField("primer_banda")
    segunda_banda = SelectField("segunda_banda")
    tercer_banda = SelectField("tercer_banda")
    radio_tol = RadioField("radio_tol")