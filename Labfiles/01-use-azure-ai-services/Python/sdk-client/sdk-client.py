from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    global ai_endpoint
    global ai_key

    # Get Configuration Settings

    load_dotenv()
    ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
    ai_key = os.getenv('AI_SERVICE_KEY')

    # Get user input (until they enter "quit")
    user_text = ''
    while user_text.lower() != 'quit':
        user_text = input('\nEnter some text ("quit" to stop)\n')
        if user_text.lower() != 'quit':
            language = get_language(user_text)
            print('Language:', language)


def get_language(text):

    # Create client using endpoint and key
    credential = AzureKeyCredential(ai_key)
    client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

    # Call the service to get the detected language
    detected_language = client.detect_language(documents=[text])[0]
    return detected_language.primary_language.name


if __name__ == "__main__":
    main()
