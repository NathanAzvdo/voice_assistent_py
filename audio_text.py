import speech_recognition as sr
import pyttsx3
def audio_to_speech(audio):
    rec = sr.Recognizer()
    try:
        if not isinstance(audio, sr.AudioData):
            raise ValueError("O argumento `audio` deve ser um objeto `AudioData`.")
        
        frase = rec.recognize_google(audio, language='pt-BR')
        return frase
    except sr.UnknownValueError:
        return 'Não foi possível entender o áudio.'
    except sr.RequestError as e:
        return f'Erro ao se conectar ao serviço de reconhecimento de voz: {e}'
    except Exception as e:
        return f'Houve um erro inesperado: {e}'

def text_to_speech(text):
    engine = pyttsx3.init()
    
    # Obter todas as vozes disponíveis
    voices = engine.getProperty('voices')
    
    # Escolher uma voz em português (verifique qual está disponível no seu sistema)
    portuguese_voice = None
    for voice in voices:
        if 'portuguese' in voice.name.lower() or 'brasil' in voice.name.lower():
            portuguese_voice = voice
            break
    
    if portuguese_voice:
        engine.setProperty('voice', portuguese_voice.id)
    else:
        print("Voz em português não encontrada. Usando a voz padrão.")
    
    # Configurar a taxa de fala e o volume (opcional)
    engine.setProperty('rate', 135)  # Velocidade da fala
    engine.setProperty('volume', 1)  # Volume (0.0 a 1.0)
    
    engine.say(text)
    engine.runAndWait()