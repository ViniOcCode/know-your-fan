from app import db

class Fan(db.Model):
    """
    Represents a fan in the database, storing personal information, interests,
    social media handles, and fan engagement data.

    Attributes:
        id (int): Primary key, auto-incremented.
        nome (str): Name of the fan, unique and required.
        idade (int): Age of the fan, unique and required.
        cpf (str): CPF (Brazilian taxpayer ID), required.
        rg (str): RG (Brazilian ID number), required.
        endereco (str): Address of the fan, required.
        email (str): Email address, required.
        interesses (str): Fan's interests, optional.
        eventos (str): Events attended or interested in, optional.
        compras (str): Purchase history, optional.
        twitter (str): Twitter handle, optional.
        instagram (str): Instagram handle, optional.
        fan_score (float): Score representing fan engagement, optional.
        twitch (str): Twitch username or channel, optional.
        documento_nome (str): Name of the document associated with the fan, optional.
    """
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