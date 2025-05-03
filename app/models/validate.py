import re 
from datetime import date, datetime

def validate_emaiL(email: str) -> bool:
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex_email, email)

def validate_cpf(cpf: str) -> bool:
    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.
    https://pt.stackoverflow.com/questions/64608/como-validar-e-calcular-o-d%C3%ADgito-de-controle-de-um-cpf - Woss
    Parâmetros:
        cpf (str): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> validate('529.982.247-25')
    True
    >>> validate('52998224725')
    False
    >>> validate('111.111.111-11')
    False
    """

    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True

def validate_document_data(form, doc_cpf, doc_birth):
    if form['cpf'] != doc_cpf:
        return False, 'CPF não bate com o do documento'

    form_age = int(form['idade'])
    birth_date = datetime.strptime(doc_birth, "%d/%m/%Y").date()
    today = date.today()
    calculated_age = today.year - birth_date.year

    if form_age != calculated_age:
        return False, 'Idade não bate com o do documento'

    # Se passou de tudo:
    return True, ''


def validate_email(email: str) -> bool:
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def validate_twitter(username: str) -> bool:
    return re.match(r'^[A-Za-z0-9_]{1,15}$', username) is not None

def validate_instagram(username: str) -> bool:
    return re.match(r'^[A-Za-z0-9._]{1,30}$', username) is not None

def validate_twitch(username: str) -> bool:
    return re.match(r'^[a-zA-Z][a-zA-Z0-9_]{3,24}$', username) is not None

if __name__ == '__main__':
    print('teste')
