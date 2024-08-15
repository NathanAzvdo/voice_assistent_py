import speech_recognition as sr 

class Voice_to_speech:

    def audio_to_speech(self, audio):
        rec = sr.Recognizer()
        frase = rec.recognize_google(audio, language='pt-BR')
        return(frase)