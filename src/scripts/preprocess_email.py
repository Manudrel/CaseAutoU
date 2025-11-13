import spacy

# Load spaCy models for Portuguese and English
MODELS = {
    'portuguese': spacy.load("pt_core_news_sm"),
    'english': spacy.load("en_core_web_sm")
}

def preprocess_email_spacy(text, lang='portuguese'):
    """Preprocess the email text using spaCy."""
    nlp = MODELS.get(lang)
    if nlp is None:
        raise ValueError(f"Language '{lang}' not supported. Use 'portuguese' or 'english'.")
    doc = nlp(text.lower())

    tokens = [
        token.lemma_ 
        for token in doc 
        if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)
