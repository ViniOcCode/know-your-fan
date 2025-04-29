from flask import Flask, Blueprint, render_template, request, jsonify
from app.models.fans import Fan
from app.models.validate import *
from app import db
from app.templates import *
import re
import os 

data = Blueprint('data', __name__)

@data.route('/', methods=['GET'])
def get_data():
    return render_template('form.html')

@data.route('/submit', methods=['POST'])
def set_data():
    document = request.files['documento']
    filename = document.filename
    path = os.path.join('app', 'controllers', 'uploads', filename)
    os.makedirs('uploads', exist_ok=True)
    document.save(path)

    if not validate_cpf(request.form['cpf']) or not validate_emaiL(request.form['email']):
        return render_template("form.html", error='CPF e/ou Email inválidos')

        new_fan = Fan(
            nome = request.form["nome"],
            idade = request.form["idade"],
            cpf = request.form["cpf"],
            endereco = request.form["endereco"],
            email=request.form["email"],
            interesses=request.form["interesses"],
            eventos=request.form["eventos"],
            compras=request.form["compras"],
            twitter=request.form["twitter"],
            instagram=request.form["instagram"],
            outra_rede=request.form["outra_rede"],
            perfil_esports=request.form["perfil_esports"],
            documento_nome=filename
        )
        try:
            db.session.add(new_fan)
            db.session.commit()
            return f"Salvo: {new_fan.nome}"
        except:
            return f'{new_fan.nome} não foi salvo'

@data.route('/fans', methods=['GET'])
def list_fans():
    fans = Fan.query.all() 
    return jsonify([{
                    'id': fan.id,
                    'nome': fan.nome,
                    'idade': fan.idade
                    } for fan in fans])