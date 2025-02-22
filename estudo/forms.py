from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import os
from werkzeug.utils import secure_filename

from estudo.models import Contato, User, Post, PostComentarios
from estudo import db, bCrypt, app

class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha =PasswordField('Senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email já cadastrado')

    def save(self):
        senha = bCrypt.generate_password_hash(self.senha.data).decode('utf-8')
        user = User(
            nome=self.nome.data, 
            sobrenome=self.sobrenome.data, 
            email=self.email.data, 
            senha=senha
        )

        db.session.add(user)
        db.session.commit()
        return user
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Entrar')

    def login(self):
        user = User.query.filter_by(email=self.email.data).first()
        
        if user:
            if bCrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                return user
            else:
                raise Exception('Senha incorreta')
        else:
            raise Exception('Usuário não cadastrado')
        
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

class PostForm(FlaskForm):
    mensagem = TextAreaField('Conteúdo', validators=[DataRequired()])
    imagem = FileField('Imagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id):
        imagem = self.imagem.data
        nome_seguro = secure_filename(imagem.filename)
        post = Post (
            mensagem=self.mensagem.data,
            user_id=user_id,
            imagem=nome_seguro
        )

        caminho = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),# Pegar a pasta que está nosso projeto
            app.config['UPLOAD_FILES'],# Definir a pasta que configuramos para UPLOAD
            'post',# a pasta que está os POST
            nome_seguro
        )

        imagem.save(caminho)
        db.session.add(post)
        db.session.commit()

class PostComentarioForm(FlaskForm):
    comentario = TextAreaField('Comentário', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id, post_id):
        comentario = PostComentarios(
            comentario=self.comentario.data, 
            user_id=user_id, 
            post_id=post_id
        )

        db.session.add(comentario)
        db.session.commit()