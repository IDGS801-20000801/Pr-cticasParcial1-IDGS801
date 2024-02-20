from wtforms import Form
from wtforms import IntegerField, SelectField, RadioField, StringField, validators

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

class DiccionarioForm(Form):
    palabra_espanhol = StringField('Español', [validators.DataRequired(message="Este campo es requerido."), 
                                          validators.length(min = 1, max = 15, message="La longitud del campo no cuadra mi buen.")])
    
    english_word = StringField('English', [validators.DataRequired(message="This field is required."), 
                                          validators.length(min = 1, max = 15, message="Does not meet the length of the field ma'boy.")])
    
    radio_language = RadioField("radio_language", choices=[('english', 'Ingles'), ('spanish', 'Español')])
    
    translate_word = StringField('Word to translate | Palabra a traducir')