# nlp.py (Phase 4)

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import random

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

class NLPProcessor:
    def __init__(self):
        # Initialize advanced NLP settings and configurations
        self.stop_words = set(stopwords.words('english'))
        self.sentiment_analyzer = SentimentIntensityAnalyzer()

    def tokenize_text(self, text):
        # Tokenize input text into words and sentences
        words = word_tokenize(text)
        sentences = sent_tokenize(text)
        return {
            "words": words,
            "sentences": sentences
        }

    def remove_stopwords(self, text):
        # Remove stopwords from the input text
        words = word_tokenize(text)
        filtered_words = [word for word in words if word.lower() not in self.stop_words]
        return " ".join(filtered_words)

    def analyze_sentiment(self, text):
        # Analyze sentiment of the input text
        sentiment_scores = self.sentiment_analyzer.polarity_scores(text)
        sentiment_label = "positive" if sentiment_scores['compound'] >= 0.05 else "negative" if sentiment_scores['compound'] <= -0.05 else "neutral"
        return f"AI Assistant: The sentiment of the text is {sentiment_label}."

    def generate_random_response(self, text):
        # Generate a random response based on input text
        responses = [
            "That's interesting. Tell me more.",
            "I see what you mean. Please continue.",
            "Fascinating! Can you elaborate?",
            "Interesting perspective. Go on.",
            "I'd like to hear more about that."
        ]
        return random.choice(responses)

# Example usage:
if __name__ == "__main__":
    nlp_module = NaturalLanguageProcessing()

    print("AI Assistant: Welcome to the advanced natural language processing module (Phase 4)!")
    while True:
        print("Options:")
        print("1. Tokenize text")
        print("2. Remove stopwords")
        print("3. Analyze sentiment of text")
        print("4. Generate a random response")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            text = input("Enter the text to tokenize: ")
            tokenization_result = nlp_module.tokenize_text(text)
            print(tokenization_result)
        elif choice == "2":
            text = input("Enter the text to remove stopwords: ")
            filtered_text = nlp_module.remove_stopwords(text)
            print(f"AI Assistant: Text after removing stopwords:\n{filtered_text}")
        elif choice == "3":
            text = input("Enter the text to analyze sentiment: ")
            sentiment_analysis_result = nlp_module.analyze_sentiment(text)
            print(sentiment_analysis_result)
        elif choice == "4":
            text = input("Enter a text prompt: ")
            random_response = nlp_module.generate_random_response(text)
            print(f"AI Assistant: {random_response}")
        elif choice == "5":
            print("AI Assistant: Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
