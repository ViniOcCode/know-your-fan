import re 
from datetime import date, datetime


def validate_cpf(cpf: str) -> bool:
    """
    https://pt.stackoverflow.com/questions/64608/como-validar-e-calcular-o-d%C3%ADgito-de-controle-de-um-cpf - Woss
    Validates a Brazilian CPF, including format and verification digits.

    Args:
        cpf (str): CPF to validate, expected in the format 999.999.999-99.

    Returns:
        bool: 
            - False if the CPF format is invalid;
            - False if the CPF does not have 11 numeric characters;
            - False if the verification digits are invalid;
            - True if the CPF is valid.
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

def validate_email(email: str) -> bool:
    """
    Validates if the given email address has a correct format.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex_email, email)

def validate_document_data(form, doc_cpf, doc_birth):
    """
    Checks if the CPF and birth date extracted from the document match the form data.

    Args:
        form (dict): Form data containing 'cpf' and 'idade'.
        doc_cpf (str): CPF extracted from the document.
        doc_birth (str): Birth date extracted from the document in DD/MM/YYYY format.

    Returns:
        tuple: (bool, str) where bool indicates if validation passed,
        and str provides an error message if validation failed.
    """
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

def validate_twitter(username: str) -> bool:
    """
    Validates if a Twitter username has a valid format.

    Args:
        username (str): Twitter username.

    Returns:
        bool: True if the username is valid (1–15 alphanumeric characters or underscores), False otherwise.
    """
    return re.match(r'^[A-Za-z0-9_]{1,15}$', username) is not None

def validate_instagram(username: str) -> bool:
    """
    Validates if an Instagram username has a valid format.

    Args:
        username (str): Instagram username.

    Returns:
        bool: True if the username is valid (1–30 characters, letters, numbers, dots, or underscores), False otherwise.
    """
    return re.match(r'^[A-Za-z0-9._]{1,30}$', username) is not None

def validate_twitch(username: str) -> bool:
    """
    Validates if a Twitch username has a valid format.

    Args:
        username (str): Twitch username.

    Returns:
        bool: True if the username is valid (starts with a letter, 4–25 characters, alphanumeric or underscores), False otherwise.
    """
    return re.match(r'^[a-zA-Z][a-zA-Z0-9_]{3,24}$', username) is not None

if __name__ == '__main__':
    print('teste')
