import tkinter as tk
from tkinter import messagebox
import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix

def preprocess_text(text):
    """
    Preprocess the text by converting it to lowercase and removing special characters.
    Args:
        text (str): Text to preprocess.
    Returns:
        str: Preprocessed text.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def is_reliable_source(source):
    """
    Check if the source is a reliable source.
    Args:
        source (str): Source to check.
    Returns:
        bool: True if the source is reliable, False otherwise.
    """
    reliable_sources = [
            "CNN",
            "BBC",
            "New York Times",
            "The Guardian",
            "Reuters",
            "Associated Press",
            "Al Jazeera",
            "NBC News",
            "CBS News",
            "ABC News",
            "Fox News",
            "Washington Post"
    ]
    return source in reliable_sources

def verify_article(article, source):
    
    article = article.lower()  # Convert the article to lowercase
    source = source.lower()    # Convert the source to lowercase

    try:
        # Preprocess the article text
        preprocessed_article = preprocess_text(article)

        # Compare the article with reliable sources
        if is_reliable_source(source):
            messagebox.showinfo("Verification Result", "The news article is classified as: real (from a reliable source)")
        else:
            # Predict the label for the article
            label = pipeline.predict([preprocessed_article])[0]

            # Print the classification result
            if label == 1:
                messagebox.showinfo("Verification Result", "The news article is classified as: real")
            else:
                messagebox.showinfo("Verification Result", "The news article is classified as: fake (not from a reliable source or matches fake news database)")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred during verification: {}".format(e))

def main():
    try:
        global pipeline
        
        # Load the training data from the CSV file
        training_data_file = 'training_news.csv'
        df = pd.read_csv(training_data_file)

        # Preprocess the text column
        df['processed_text'] = df['text'].apply(preprocess_text)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(df['processed_text'], df['label'], test_size=0.2, random_state=42)

        # Create a pipeline with TF-IDF vectorizer and logistic regression classifier
        pipeline = Pipeline([
            ('vectorizer', TfidfVectorizer()),
            ('classifier', LogisticRegression())
        ])

        # Train the model
        pipeline.fit(X_train, y_train)

        # Evaluate the model on the testing set
        y_pred = pipeline.predict(X_test)

        # Print the classification report and confusion matrix
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        # Create a GUI window
        window = tk.Tk()
        window.title("News Article Verification")
        
        # Create labels and entry fields for the article and source
        article_label = tk.Label(window, text="Enter a news article:")
        article_label.pack()
        article_entry = tk.Entry(window)
        article_entry.pack()

        source_label = tk.Label(window, text="Enter the source of the news article:")
        source_label.pack()
        source_entry = tk.Entry(window)
        source_entry.pack()

        # Create a button to verify the article
        verify_button = tk.Button(window, text="Verify Article", command=lambda: verify_article(article_entry.get(), source_entry.get()))
        verify_button.pack()

        # Run the GUI main loop
        window.mainloop()

    except Exception as e:
        # Handle any exception that occurs during the verification process
        messagebox.showerror("Error", "An error occurred during verification: {}".format(e))

if __name__ == '__main__':
    main()
