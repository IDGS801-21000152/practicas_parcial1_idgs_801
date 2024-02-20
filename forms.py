from wtforms import Form
from wtforms import DecimalField, IntegerField, StringField, RadioField
from wtforms import validators

class DistanciaForm(Form):
    x1 = IntegerField('coordenada x1')
    x2 = IntegerField('coordenada x2')
    y1 = IntegerField('coordenada y1')
    y2 = IntegerField('coordenada y2')
    
class ResitenciaForm(Form):
    primerBanda = StringField('Banda 1')
    segundaBanda = StringField('Banda 2')
    tercerBanda = StringField('Banda 3')
    tolerancia = StringField('Tolerancia')
    valorMinimo = DecimalField('Valor mínimo')
    valorMaximo = DecimalField('Valor máximo')

class DiccionarioForm(Form):
    palabraIngles = StringField('Palabra en inglés', [
        validators.DataRequired(message='Required Field'),
    ])
    palabraEspaniol = StringField('Palabra en español', [
        validators.DataRequired(message='Campo requerido')
    ])
    palabraABuscar = StringField('Word to Translate / palabra a traducir', [
        validators.DataRequired(message='campo requerido / required field')
    ])
    idioma = RadioField('Idioma a traducir', choices=[('espaniol', 'Español'), ('ingles', 'Inglés')], 
        validators=[validators.InputRequired(message='Selecciona un idioma / Select a language')])
    resultado = StringField('Resultado / Response')