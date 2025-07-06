import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import string

nltk.download('stopwords')
from nltk.corpus import stopwords

def clean_text(text):
    # TODO: 
    # 1) convert text to lowercase: text.lower()
    # 2) remove punctuation (e.g., use string.punctuation)
    # 3) remove stopwords from nltk.corpus.stopwords.words('english')
    # 4) return the cleaned text as a single string
    pass  # Remove this line after implementing

def prepare_data():
    # Load data
    df = pd.read_csv("data/raw_data.csv")
    
    # Clean text
    df['text'] = df['text'].apply(clean_text)

    # Vectorize text
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=10000)
    X = vectorizer.fit_transform(df['text'])
    y = df['label']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, vectorizer
