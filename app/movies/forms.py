from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class MovieForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    anio = IntegerField('Año', validators=[DataRequired(), NumberRange(min=1900, max=2100)])
    genero = StringField('Género', validators=[DataRequired()])
    duracion_min = IntegerField('Duración (minutos)', validators=[NumberRange(min=1)])
    director = StringField('Director')
    reparto = TextAreaField('Reparto Principal')
    sinopsis = TextAreaField('Sinopsis', validators=[DataRequired()])
    imagen_url = StringField('URL de la imagen')
    submit = SubmitField('Guardar')

class CommentForm(FlaskForm):
    contenido = TextAreaField('Comentario', validators=[DataRequired(), Length(min=3, max=500)])
    submit = SubmitField('Enviar')

class RatingForm(FlaskForm):
    estrellas = SelectField(
        'Calificación',
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
        validators=[DataRequired()],
        coerce=int
    )
    submit = SubmitField('Calificar')

class TopicForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(min=3, max=100)])
    contenido = TextAreaField('Contenido', validators=[DataRequired(), Length(min=10, max=2000)])
    submit = SubmitField('Crear Tema')

class ReplyForm(FlaskForm):
    contenido = TextAreaField('Respuesta', validators=[DataRequired(), Length(min=3, max=1000)])
    submit = SubmitField('Responder')
