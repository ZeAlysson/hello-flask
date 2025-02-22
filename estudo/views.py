from estudo import app, db
from flask import render_template, request, redirect, url_for, flash
from estudo.models import Contato, Post
from estudo.forms import ContatoForm, UserForm, LoginForm, PostForm
from flask_login import login_user, logout_user, current_user

@app.route('/', methods=['GET', 'POST'])  # route() decorator to tell Flask what URL should trigger our function
def homepage():
    user = 'José'
    age = 22

    form = LoginForm()

    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)

    context = {
        'user': user,
        'age': age
    }


    return render_template('index.html', context=context, form=form)  # render a template

@app.route('/sobre/')
def about():
    return render_template('about.html')

#######Formato Não Recomendado#########
@app.route('/contato_old/', methods=['GET', 'POST'])
def contato_old():
    context = {}

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})
        print('GET:', pesquisa)

    if request.method == 'POST':
        name = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        message = request.form['mensagem']
    
        contato = Contato(name=name, email=email, assunto=assunto, message=message)
        db.session.add(contato)
        db.session.commit()


    return render_template('contato_old.html', context=context)
#######################################

@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    

    form = ContatoForm()

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template('contato.html', form=form)

@app.route('/contatos/lista/')
def lista_contatos():

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Contato.query.order_by('name')

    if pesquisa != '':
        dados = dados.filter_by(name=pesquisa)
    
    context = {
        'dados': dados.all()
    }

    return render_template('lista_contatos.html', context=context)


@app.route('/contatos/<int:id>/')
def detalhe_contato(id):
    obj = Contato.query.get(id)



    return render_template('detalhe_contato.html', obj=obj)

@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro():

    form = UserForm()

    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    
    return render_template('cadastro.html', form=form)

@app.route('/sair/')
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/post/novo/', methods=['GET', 'POST'])
def novo_post():
    if not current_user.is_authenticated:
        flash('Você precisa estar logado para criar um novo post.', 'warning')
        return redirect(url_for('homepage'))

    form = PostForm()

    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('homepage'))

    return render_template('novo_post.html', form=form)

@app.route('/post/lista/', methods=['GET'])
def lista_posts():
    posts = Post.query.all()

    context = {
        'posts': posts
    }

    return render_template('lista_posts.html', context=context)