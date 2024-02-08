from wtforms import Form
from wtforms import DecimalField, IntegerField, StringField


class DistanciaForm(Form):
    x1 = IntegerField('coordenada x1')
    x2 = IntegerField('coordenada x2')
    y1 = IntegerField('coordenada y1')
    y2 = IntegerField('coordenada y2')
    
class ResitenciaForm(Form):
    primerBanda = StringField('Banda 1')
    vPrimerBanda = IntegerField()
    segundaBanda = StringField('Banda 2')
    vSegundaBanda = IntegerField()
    tercerBanda = StringField('Banda 3')
    vTercerBanda = IntegerField()
    tolerancia = StringField('Tolerancia')
    vTolerancia = DecimalField()
    valorMinimo = DecimalField('Valor mínimo')
    valorMaximo = DecimalField('Valor máximo')
    