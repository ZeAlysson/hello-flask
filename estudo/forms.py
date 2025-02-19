from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

from estudo.models import Contato
from estudo import db

class ContatoForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    message = TextAreaField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        contato = Contato(
            name=self.name.data, 
            email=self.email.data, 
            assunto=self.assunto.data, 
            message=self.message.data
        )

        db.session.add(contato)
        db.session.commit()