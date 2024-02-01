from wtforms import Form
from wtforms import DecimalField, IntegerField


class DistanciaForm(Form):
    x1 = IntegerField('coordenada x1')
    x2 = IntegerField('coordenada x2')
    y1 = IntegerField('coordenada y1')
    y2 = IntegerField('coordenada y2')