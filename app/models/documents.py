from pathlib import Path 
from pdf2image import convert_from_path
import easyocr
import re

def checkFile(path: str, extensions: tuple = ('.pdf',)) -> list:
    """
    Renames files in the specified directory to lowercase with underscores, 
    and returns a list of files matching the given extensions.

    Args:
        path (str): Path to the directory to check.
        extensions (tuple, optional): Valid file extensions. Defaults to ('.pdf',).

    Returns:
        list: List of Path objects for the valid files found.
    """
    path_obj = Path(path)
    valid_files = []

    for item in path_obj.glob('*'):
        new_name = str(item.name).lower().replace(' ', '_')
        new_path = item.with_name(new_name)
        item.rename(new_path)

        if new_path.suffix in extensions:
            valid_files.append(new_path)

    return valid_files

def pdfToImg(path: str) -> list:
    """
    Converts PDF files in the directory to high-resolution JPEG images.

    Args:
        path (str): Path to the directory containing the PDF files.

    Returns:
        list: List of paths to the generated JPEG images.
    """
    pdf_files = checkFile(path, extensions=('.pdf',)) 
    saved_images = []

    for pdf_path in pdf_files:
        pages = convert_from_path(pdf_path, dpi=500)
        
        for i, page in enumerate(pages):
            image_path = Path(path) / f"img_{pdf_path.stem}_page{i}.jpg"
            page.save(image_path, "JPEG")
            saved_images.append(image_path)

    return saved_images

def checkDocument(path: str) -> tuple:
    """
    Converts PDFs to images, runs OCR on the images, and tries to extract CPF, RG, and birth date.

    Args:
        path (str): Path to the directory containing the documents.

    Returns:
        tuple: A tuple (cpf, rg, birth) with the extracted data, or None if not found.
    """
    # Gera imagens dos PDFs
    pdfToImg(path)

    # Agora procura pelas imagens
    image_files = checkFile(path, extensions=('.png', '.jpeg', '.jpg')) 
    reader = easyocr.Reader(['pt'])
    cpf = None
    rg = None

    for image_path in image_files:
        ocr_results = reader.readtext(str(image_path))
        
        for _, text, conf in ocr_results:
            if conf < 0.5:
                continue

            text_clean = text.strip().upper()

            # Tenta achar CPF por regex
            cpf_match = re.search(r'\d{9}/\d{2}', text_clean)
            if cpf_match:
                cpf = correct_cpf(cpf_match.group())

            # Tenta achar RG por regex
            rg_match = re.search(r'\b\d{2}\.\d{3}\.\d{3}-\d{1}\b', text_clean)
            if rg_match:
                rg = rg_match.group()
            
            birth_match = re.search(r'\d{2}/\d{2}/\d{4}', text_clean)
            if birth_match:
                birth = birth_match.group()

    return cpf, rg, birth

def correct_cpf(text: str) -> str:
    """
    Cleans and formats an extracted CPF number to the standard format XXX.XXX.XXX-XX.

    Args:
        text (str): Raw text containing the CPF.

    Returns:
        str: Properly formatted CPF, or the original text if it doesn't match the expected pattern.
    """
    text = text.replace('/', '-').replace('.', '').replace(' ', '')
    if re.fullmatch(r'\d{9}-\d{2}', text):
        # Reinsere pontos no formato padrão
        return f"{text[:3]}.{text[3:6]}.{text[6:9]}-{text[10:]}"
    return text  # retorna como está se não bater o padrão esperado

if __name__ == '__main__':
    checkDocument()