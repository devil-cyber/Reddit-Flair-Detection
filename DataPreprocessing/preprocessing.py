import re
import nltk
from bs4 import BeautifulSoup
nltk.download('wordnet')
nltk.download('words')
nltk.download('stopwords')

from nltk.stem import WordNetLemmatizer

from nltk.corpus import stopwords


class Preprocessing:
    def __init__(self, message):
        self.message = message

    def text_cleaning(self):
        z = self.message
        stop_word = stopwords.words('english')
        BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
        lem = WordNetLemmatizer()
        text = BeautifulSoup(z).text
        text = text.lower()
        text = re.sub(r'\W+', ' ', text)
        text = BAD_SYMBOLS_RE.sub(' ', text)
        text = ' '.join(lem.lemmatize(word) for word in text.split() if word not in stop_word)
        return text
