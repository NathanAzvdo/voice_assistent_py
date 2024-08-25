import speech_recognition as sr

class VoiceInput:
    def record(self):
        rec = sr.Recognizer()
        try:
            with sr.Microphone(device_index=3) as mic:
                rec.adjust_for_ambient_noise(mic)
                print("Qual sua dúvida?")
                audio = rec.listen(mic)
                print("Áudio capturado com sucesso.")
                return audio
        except sr.UnknownValueError:
            print('Não foi possível entender o áudio.')
        except sr.RequestError as e:
            print(f'Erro ao se conectar ao serviço de reconhecimento de voz: {e}')
        except Exception as e:
            print(f'Houve um erro inesperado: {e}')
