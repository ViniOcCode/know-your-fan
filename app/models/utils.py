from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np

# Carregar modelo e tokenizer
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Labels do modelo
labels = ['Negative', 'Neutral', 'Positive']

def fan_analyse(texto: str) -> int:
    """
    Analyzes a text to compute a fan engagement score using a pretrained model.

    Args:
        texto (str): Input text to be analyzed.

    Returns:
        int: Calculated fan score (based on the 'Positive' label percentage).
    """
    # Tokenização com truncamento e padding
    if texto == None or texto.strip() == '':
        return 0

    encoded_input = tokenizer(texto, return_tensors='pt', truncation=True, padding=True, max_length=212)
    
    # Forward
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    resultado = dict(zip(labels, np.round(scores, 4)))
    resultado['fan_score'] = round(resultado['Positive'] * 100)
    return resultado

def calculate_fan_score(form_data: dict) -> int:
    """
    Calculates the total fan score based on form data, analyzing interests, events,
    purchases, and presence on social media.

    Args:
        form_data (dict): Dictionary containing fan information, including
            'interesses', 'eventos', 'compras', 'twitter', 'instagram', and 'twitch'.

    Returns:
        int: Total calculated fan score.
    """
    score = 0
    if form_data['interesses']:
        score += fan_analyse(form_data['interesses'])['fan_score']
    if form_data['eventos']:
        score += fan_analyse(form_data['eventos'])['fan_score']
    if form_data['compras']:
        score += fan_analyse(form_data['compras'])['fan_score']
    if form_data['twitter'] or form_data['instagram'] or form_data['twitch']:
        score += 3
    return score

if __name__ == '__main__':
    print(fan_analyse('teamo furia'))