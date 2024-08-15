import speech_recognition as sr 

class Voice_input:
    def record(self):
        rec = sr.Recognizer()
        try:
            with sr.Microphone(device_index=3) as mic:
                rec.adjust_for_ambient_noise(mic)
                print("Qual sua dúvida?")
                audio = rec.listen(mic)
                return audio
        except:
            print('Houve algum erro para captar sua voz! :(')
