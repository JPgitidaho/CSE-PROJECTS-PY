import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


def extract_features():
    # Read the CSV file with the data
    data = pd.read_csv('PROYECT_PY/dataset/conjunto_datos.csv')

    # Get the text and label columns
    X = data['news']
    y = data['label']

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X)

    return X, y, vectorizer


def classify_news(news):
    # Load the trained model
    clf = joblib.load('PROYECT_PY/models/trained_model.pkl')

    # Load the vectorizer
    vectorizer = joblib.load('PROYECT_PY/models/vectorizer.pkl')

    # Preprocess the news and convert it into features
    features = vectorizer.transform([news])

    # Classify the news
    prediction = clf.predict(features)

    return prediction[0]


def main():
    new_news = input("Enter the news to verify: ")
    resultado = classify_news(new_news)

    if resultado == 1:
        print("The news is fake.")
    else:
        print("The news is true.")


if __name__ == "__main__":
    main()
