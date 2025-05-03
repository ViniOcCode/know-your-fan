from app import db

class Fan(db.Model):
    __tablename__ = 'fans'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    idade = db.Column(db.Integer, unique=True, nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    rg = db.Column(db.String(14), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    interesses = db.Column(db.Text, nullable=True)
    eventos = db.Column(db.Text, nullable=True)
    compras = db.Column(db.Text, nullable=True)

    twitter = db.Column(db.String(120), nullable=True)
    instagram = db.Column(db.String(120), nullable=True)
    fan_score = db.Column(db.Float, nullable=True)

    twitch = db.Column(db.String(250), nullable=True)
    documento_nome = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Fan {self.nome}>'