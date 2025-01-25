import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk


def preprocess_text(text):
    # Prepare natural language processing tools
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('stopwords')
    # Process the text through tokenization, stopword removal, and lemmatization
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)
