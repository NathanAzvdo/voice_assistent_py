from voice_input import VoiceInput
from audio_text import audio_to_speech, text_to_speech
from api_googleAI import genAI

def main():
    voice_input = VoiceInput()
    api_client = genAI()

    text_to_speech('Basta falar SAIR para finalizar a conversa')

    while True:
        audio = voice_input.record()
        text = audio_to_speech(audio)

        if text.strip().lower() == 'sair':
            text_to_speech('Encerrando chat!')
            break

        # Obtém resposta da API
        response = api_client.process_message(text)
        text_to_speech(response)
        

if __name__ == "__main__":
    main()