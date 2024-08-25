from voice_input import VoiceInput
from voice_to_speech import audio_to_speech
from api_googleAI import genAI

def main():
    voice_input = VoiceInput()
    api_client = genAI()

    print('Basta falar SAIR para finalizar a conversa')

    while True:
        # Captura o áudio
        audio = voice_input.record()
        # Converte o áudio em texto
        text = audio_to_speech(audio)
        print(f'Você disse: {text}')

        if text.strip().lower() == 'sair':
            print("Encerrando chat!")
            break

        # Obtém resposta da API
        response = api_client.process_message(text)
        print(f'Resposta da IA: {response}')

if __name__ == "__main__":
    main()