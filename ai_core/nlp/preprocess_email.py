import spacy
from langdetect import detect

try:
    nlp_en = spacy.load("en_core_web_sm")
except Exception:
    nlp_en = None
try:
    nlp_pt = spacy.load("pt_core_news_sm")
except Exception:
    nlp_pt = None

# Choose the appropriate NLP model based on detected language
def choose_nlp(text: str) -> spacy.language.Language:
    try:
        lang = detect(text)
    except Exception:
        lang = 'xx'
    if lang.startswith('pt') and nlp_pt:
        return nlp_pt
    if lang.startswith('en') and nlp_en:
        return nlp_en
    return nlp_en or nlp_pt or spacy.blank("xx")

# Preprocess the email text
def preprocess_text(text: str) -> str:
    nlp = choose_nlp(text)
    doc = nlp(text.lower()) 
    tokens = [t.lemma_.strip() for t in doc if not t.is_stop and t.is_alpha]
    return " ".join(tokens)


if __name__ == "__main__":
    sample_text = (
        "Dear Support Team,\n\n"
        "I would like updates on open cases."
        "\n\n"
        "Sincerely, \nEmanuel Duarte"
    )
    print(preprocess_text(sample_text))