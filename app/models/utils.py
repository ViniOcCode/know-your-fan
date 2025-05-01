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

if __name__ == '__main__':
    print(fan_analyse('teamo furia'))