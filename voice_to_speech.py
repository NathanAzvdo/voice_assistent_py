import speech_recognition as sr

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
