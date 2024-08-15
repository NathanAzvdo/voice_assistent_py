import openai
import os
import time
from dotenv import load_dotenv

class api_openai():
    
    load_dotenv()
    key = os.getenv('OPENAI_KEY')
    openai.api_key= key

    def response(self, text):
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model='gpt-3.5-turbo',
                    messages=[{'role': 'user', 'content': text}]
                )
                return response
            except openai.error.RateLimitError:
                print("tentando conectar a OpenAI...")
                time.sleep(5)