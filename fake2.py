import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score
import pickle


def extract_features():
    # Cargar el conjunto de datos
    data = pd.read_csv('PROYECT_PY/models/conjunto_datos.csv')

    # Dividir los datos en características (X) y etiquetas (y)
    X = data['texto']
    y = data['etiqueta']

    # Crear un objeto TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

    # Transformar los datos de texto en vectores de características
    X = vectorizer.fit_transform(X)

    return X, y, vectorizer


def train_model(X, y):
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Crear un clasificador PassiveAggressiveClassifier
    classifier = PassiveAggressiveClassifier(max_iter=50)

    # Entrenar el modelo
    classifier.fit(X_train, y_train)

    # Predecir las etiquetas para el conjunto de prueba
    y_pred = classifier.predict(X_test)

    # Calcular la precisión del modelo
    accuracy = accuracy_score(y_test, y_pred)
    print("Precisión del modelo: {:.2f}%".format(accuracy * 100))

    return classifier


def save_model(classifier, vectorizer):
    # Guardar el modelo entrenado en un archivo pickle
    with open('PROYECT_PY/models/trained_model.pkl', 'wb') as file:
        pickle.dump((classifier, vectorizer), file)


def classify_news(news):
    # Cargar el modelo entrenado desde el archivo pickle
    with open('PROYECT_PY/models/trained_model.pkl', 'rb') as file:
        classifier, vectorizer = pickle.load(file)

    # Preprocesar la noticia de entrada
    processed_news = vectorizer.transform([news])

    # Clasificar la noticia como genuina o falsa
    prediction = classifier.predict(processed_news)

    if prediction[0] == 0:
        return "Genuina"
    else:
        return "Falsa"


def main():
    # Extraer características del conjunto de datos
    X, y, vectorizer = extract_features()

    # Entrenar el modelo y guardar en el archivo trained_model.pkl
    classifier = train_model(X, y)
    save_model(classifier, vectorizer)

    # Solicitar al usuario una noticia para verificar
    nueva_noticia = input("Ingresa la noticia a verificar: ")
    resultado = classify_news(nueva_noticia)
    print("La noticia ingresada es:", resultado)


if __name__ == '__main__':
    main()
