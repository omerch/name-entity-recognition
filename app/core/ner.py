import spacy
from spacy.lang.en.examples import sentences
from app.config import get_settings
settings = get_settings()

def get_ner_model():
    # Load the model
    ner = spacy.load("en_core_web_sm")
    return ner
