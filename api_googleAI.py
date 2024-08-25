import google.generativeai as genai
from dotenv import load_dotenv
import os

class genAI:
    def __init__(self):
        self._load_environment()
        self._configure_genai()
        self.model = self._get_model()
        self.chat = self.model.start_chat(history=[])

    def _load_environment(self):
        load_dotenv()

    def _configure_genai(self):
        GOOGLE_API_KEY = os.getenv("google_api_key")
        if not GOOGLE_API_KEY:
            raise ValueError("A chave da API do Google não está definida.")
        genai.configure(api_key=GOOGLE_API_KEY)

    def _get_model(self):
        model_name = 'gemini-1.5-pro-latest'
        return genai.GenerativeModel(model_name)

    def process_message(self, text):
        response = self.chat.send_message(text)
        return response.text

    def start_chat(self):
        """Inicia o chat e processa as perguntas até o usuário dizer 'sair'."""
        print('Basta falar SAIR para finalizar a conversa')
        while True:
            text = input("Qual sua dúvida? ").strip().lower()
            if text == 'sair':
                break
            response = self.process_message(text)
            print(f'{response}\n---------------------------------------------------------')
        print("Encerrando chat!")
