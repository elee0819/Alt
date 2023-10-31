# Import your modules here
import openai
from self_modification import SelfModification
from file_operations import FileOperations
from nlp import NLPProcessor
from ml import MLProcessor
from dan import DataAnalyzer
from memory_learning import Memory, Learning
from task_automation import TaskAutomation
from recommendation_engine import RecommendationEngine
from advanced_ai import Advancedai
from voice_synthesis import VoiceSynthesis


# Define your OpenAI API key here
OPENAI_API_KEY = "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"

class AIAssistant:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key

    def greet(self):
        return "Welcome to your AI assistant! How can I assist you today?"

    def chat_with_gpt(self, user_input):
        if not self.openai_api_key:
            self.set_openai_api_key()

        # Configure OpenAI API with your API key
        openai.api_key = self.openai_api_key

        # Use AI model to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )

        return response.choices[0].text.strip()

    def execute_request(self):
        while True:
            print(self.greet())
            print("Menu:")
            print("1. Make a request")
            print("2. Exit")
            
            choice = input("Enter your choice (1/2): ")
            
            if choice == "1":
                user_request = input("You: ")
                response = self.chat_with_gpt(user_request)
                print(f"AI Assistant: {response}")
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def set_openai_api_key(self):
        if not self.openai_api_key:
            self.openai_api_key = input("Please enter your OpenAI API key: ")

def main():
    ai_assistant = AIAssistant(openai_api_key=OPENAI_API_KEY)

    ai_assistant.execute_request()

    print("Goodbye! Feel free to return if you have more questions.")

if __name__ == "__main__":
    main()

