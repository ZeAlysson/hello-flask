from estudo import app, db
from flask import render_template, request, redirect, url_for
from estudo.models import Contato

@app.route('/')  # route() decorator to tell Flask what URL should trigger our function
def homepage():
    user = 'José'
    age = 22

    context = {
        'user': user,
        'age': age
    }


    return render_template('index.html', context=context)  # render a template

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
    from estudo.forms import ContatoForm

    form = ContatoForm()

    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template('contato.html', form=form)