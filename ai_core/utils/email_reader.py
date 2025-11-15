import os
from PyPDF2 import PdfReader

def email_reader(file_path: str) -> str:
    """Reads .txt and .pdf files and returns extracted text."""

    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    try:
        if file_extension == '.txt':
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

        elif file_extension == '.pdf':
            reader = PdfReader(file_path)
            content = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    content += page_text
            return content

        else:
            raise ValueError("Unsupported file format. Provide .txt or .pdf.")

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    except Exception as e:
        raise Exception(f"Error reading file: {e}")
