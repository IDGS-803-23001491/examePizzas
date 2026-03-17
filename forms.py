from wtforms import Form
from wtforms import StringField,IntegerField, DateField, RadioField, SelectMultipleField, SelectField
from wtforms import validators
from wtforms.widgets import ListWidget, CheckboxInput

class PedidoForm(Form):
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4,max=20,message='Ingrese nombre entre 4 y 20')
    ])
    direccion = StringField('Direccion',[
        validators.DataRequired(message='El campo es requerido')
    ])
    telefono = StringField('Telefono',[
        validators.DataRequired(message='El campo es requerido')
    ])
    fecha = DateField('Fecha',[
        validators.DataRequired(message='El campo es requerido')
    ],format='%Y-%m-%d')

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()
    
class PizzaForm(Form):
    tamano = RadioField(
        'Tamaño',validators=[
        validators.DataRequired(message='El campo es requerido')
    ],
        choices=[
            ('Chica', 'Chica $40'),
            ('Mediana','Mediana $80'),
            ('Grande', 'Grande $120')
        ])
    ingredientes = MultiCheckboxField(
        'Ingredientes',
        choices=[('Jamón', 'Jamón $10'), ('Piña', 'Piña $10'), ('Champiñones', 'Champiñones $10')]
    )
    cantidad = IntegerField('Cantidad',[
        validators.DataRequired(message='El campo es requerido')
    ])

class ConsultaForm(Form):
    dia = SelectField(
        'Día',
        choices=[
            (0, 'Lunes'),
            (1, 'Martes'),
            (2, 'Miércoles'),
            (3, 'Jueves'),
            (4, 'Viernes'),
            (5, 'Sábado'),
            (6, 'Domingo')
        ],
        coerce=int
    )

    mes = SelectField(
        'Mes',
        choices=[
            (1, 'Enero'),
            (2, 'Febrero'),
            (3, 'Marzo'),
            (4, 'Abril'),
            (5, 'Mayo'),
            (6, 'Junio'),
            (7, 'Julio'),
            (8, 'Agosto'),
            (9, 'Septiembre'),
            (10, 'Octubre'),
            (11, 'Noviembre'),
            (12, 'Diciembre')
        ],
        coerce=int
    )