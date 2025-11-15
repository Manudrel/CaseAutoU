from ai_core.agents.category_classifier import get_category
from ai_core.agents.response_generator import get_response
from ai_core.nlp.preprocess_email import preprocess_text
from ai_core.utils.email_reader import email_reader


async def process_email(text: str, file_path: str | None = None) -> dict:
    """This function processes an email message by reading its content,
    pre-processing the text, classifying its category, and generating a response.
    To facilitate the integration with different parts of the application."""
    content = text or ""
    
    # Reading file content if file path is provided
    if file_path:
        file_text = email_reader(file_path)
        content += "\n\n" + file_text

    # Preprocess the text
    processed = preprocess_text(content)

    # Classify the message
    category = await get_category(processed)

    # Generate a response based on the classified category
    if(category in ["Produtivo", "Improdutivo", "Productive","Unproductive"]):  
        response = await get_response(processed, category=category)
        return {
            "category": category,
            "ai_response": response
        }
    
    return {
        "category": "It was not possible to define.",     
        "ai_response": "It was not possible to generate a response."
    }
        
