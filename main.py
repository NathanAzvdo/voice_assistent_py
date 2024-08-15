from voice_input import Voice_input
from voice_to_speech import Voice_to_speech
from api_openai import api_openai

Input = Voice_input()
speech = Voice_to_speech()
gpt = api_openai()

audio = Input.record()
text = speech.audio_to_speech(audio)
print(text)
print(gpt.response(text))