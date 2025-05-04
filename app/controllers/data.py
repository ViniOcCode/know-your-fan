from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError
from app.models.fans import Fan
from app.models.validate import *
from app.models.utils import *
from app.models.documents import *
from app import db
from app.templates import *
from pathlib import Path
import os 

data = Blueprint('data', __name__)

@data.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        cpf = request.form['cpf']
        fan = Fan.query.filter_by(cpf=cpf).first()
        if fan:
            return redirect(url_for('data.list_fans', fan_id=fan.id))
        else:
            error = 'CPF não encontrado. Verifique ou cadastre-se.'
    return render_template('login.html', error=error)


@data.route('/form', methods=['GET'])
def get_data():
    return render_template('form.html', form=request.form)

@data.route('/submit', methods=['POST'])
def register():
    form = request.form
    print(type(form))

    if not validate_email(form['email']):
        return render_template('form.html', error='Email inválido', form=form)

    if not validate_twitter(form['twitter']):
        return render_template('form.html', error='Twitter inválido', form=form)

    if not validate_instagram(form['instagram']):
        return render_template('form.html', error='Instagram inválido', form=form)

    if not validate_twitch(form['twitch']):
        return render_template('form.html', error='Twitch inválido', form=form)

    document = request.files['documento']
    filename = None
    doc_cpf = rg = doc_birth = ''

    if not document:
        return render_template('form.html', error='Documento não foi enviado.', form=form)

    filename = document.filename
    dir_path = Path('app/controllers/uploads')
    os.makedirs(dir_path, exist_ok=True)
    path = dir_path / filename
    document.save(path)
        
    # Aqui chamamos checkDocument UMA VEZ
    doc_cpf, rg, doc_birth = checkDocument(dir_path)

    # Validamos com os dados já lidos
    valid, error_msg = validate_document_data(form, doc_cpf, doc_birth)

    if not valid:
        return render_template('form.html', error=error_msg, form=form)

    fan_score = calculate_fan_score(form)
    try:
        new_fan = Fan(
            nome=form['nome'],
            idade=form['idade'],
            cpf=form['cpf'],
            rg=rg,
            endereco=form['endereco'],
            email=form['email'],
            interesses=form['interesses'],
            eventos=form['eventos'],
            compras=form['compras'],
            fan_score=fan_score,
            twitter=form['twitter'],
            instagram=form['instagram'],
            twitch=form['twitch'],
            documento_nome=filename
        )

        db.session.add(new_fan)
        db.session.commit()
        return redirect(url_for('data.list_fans'))
    except IntegrityError:
        return render_template('form.html', error='CPF já cadastrado!', form=form)


@data.route('/fans', methods=['GET'])
def list_fans():
    fans = Fan.query.order_by(Fan.fan_score.desc()).all() 
    return render_template('fans_table.html', fans=fans)

@data.route('/termos', methods=['GET'])
def termos():
    return render_template('tos.html')
