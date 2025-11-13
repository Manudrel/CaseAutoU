import os
from PyPDF2 import PdfReader

def email_reader(file_path: str) -> str:
    """Reads the content of an email file.
    
    Args:
        file_path (str): The path to the email file.
        that email can be a .txt or .pdf file.
    """
    
    _, file_extension = os.path.splitext(file_path)
    try:    
        if file_extension == '.txt':
            with open(file_path, 'r') as file:
                content = file.read()
        elif file_extension == '.pdf':
            reader = PdfReader(file_path)
            content = ""
        else:
            raise ValueError("Unsupported file format. Please provide a .txt or .pdf file.")
        
        for page in reader.pages:
            content += page.extract_text()
        return content
    
    except Exception as e:
        raise Exception (f"An error occurred while reading the file: {e}")
    except FileNotFoundError: # type: ignore
        raise FileNotFoundError(f"File not found at {file_path}")