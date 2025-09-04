import re
from typing import List
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

_WORD_RE = re.compile(r"[A-Za-z']+")
_URL_RE = re.compile(r"http\S+|www\.\S+")
_MENTION_RE = re.compile(r"@\w+")
_DIGIT_RE = re.compile(r"\d+")
_PUNCT_RE = re.compile(r"[^\w\s']")

_nltk_ready = False
_lemmatizer = None
_stopwords = set()

def ensure_nltk():
    global _nltk_ready, _lemmatizer, _stopwords
    if _nltk_ready:
        return
    try:
        nltk.data.find("corpora/wordnet")
        nltk.data.find("corpora/stopwords")
        nltk.data.find("omw-1.4")
    except LookupError:
        nltk.download("wordnet")
        nltk.download("stopwords")
        nltk.download("omw-1.4")
    _lemmatizer = WordNetLemmatizer()
    _stopwords = set(stopwords.words("english"))
    _nltk_ready = True

def preprocess_text(text: str) -> str:
    """
    Mirror your notebook preprocessing:
    - lowercase
    - strip urls, @mentions, digits, punctuation
    - tokenize, lemmatize, remove stopwords
    """
    ensure_nltk()
    txt = text.lower()
    txt = _URL_RE.sub(" ", txt)
    txt = _MENTION_RE.sub(" ", txt)
    txt = _DIGIT_RE.sub(" ", txt)
    txt = _PUNCT_RE.sub(" ", txt)

    tokens: List[str] = _WORD_RE.findall(txt)
    lemmas = [_lemmatizer.lemmatize(t) for t in tokens if t not in _stopwords]
    return " ".join(lemmas).strip()
