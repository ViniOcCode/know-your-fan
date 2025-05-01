from flask import Blueprint, render_template, request, jsonify
from app.models.fans import Fan
from app.models.validate import *
from app.models.utils import *
from app.models.documents import checkDocument
from app import db
from app.templates import *
from pathlib import Path
import re
import os 

data = Blueprint('data', __name__)

@data.route('/', methods=['GET'])
def get_data():
    return render_template('form.html')

@data.route('/submit', methods=['POST'])
def set_data():
    if not validate_emaiL(request.form['email']):
        return render_template("form.html", error='Email inválido')

    document = request.files['documento']
    
    # creation and checking file
    if document:
        filename = document.filename
        dir_path = Path("app/controllers/uploads")
        path = os.path.join(dir_path, filename)
        os.makedirs(f'{dir_path}', exist_ok=True)
        document.save(path)
        cpf, rg = checkDocument(dir_path)

    if rg == None:
        return render_template("form.html", error='A imagem fornecida não é um RG ou está em qualidade baixa')

    # CPF check
    if cpf != request.form['cpf'] or not validate_cpf(request.form['cpf']):
        return render_template("form.html", error='CPF inválido')

    if request.form["interesses"]  or request.form["eventos"] or request.form["compras"]:
        interesses_score = fan_analyse(request.form['interesses'])
        eventos_score = fan_analyse(request.form['eventos'])
        compras_score = fan_analyse(request.form['compras'])

        fan_score = interesses_score['fan_score'] + eventos_score['fan_score'] + compras_score['fan_score']
    
        new_fan = Fan(
            nome = request.form["nome"],
            idade = request.form["idade"],
            cpf = request.form["cpf"],
            rg = rg,
            endereco = request.form["endereco"],
            email=request.form["email"],
            interesses=request.form["interesses"],
            eventos=request.form["eventos"],
            compras=request.form["compras"],
            fan_score=fan_score,
            twitter=request.form["twitter"],
            instagram=request.form["instagram"],
            outra_rede=request.form["outra_rede"],
            perfil_esports=request.form["perfil_esports"],
            documento_nome=filename
        )

        db.session.add(new_fan)
        db.session.commit()
        return f"Salvo: {new_fan.nome}"

@data.route('/fans', methods=['GET'])
def list_fans():
    fans = Fan.query.all() 
    return jsonify([{
                    'id': fan.id,
                    'nome': fan.nome,
                    'idade': fan.idade,
                    'fan_score': fan.fan_score
                    } for fan in fans])