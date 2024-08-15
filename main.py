from voice_input import Voice_input
from voice_to_speech import Voice_to_speech

Input = Voice_input()
speech = Voice_to_speech()

audio = Input.record()
print(speech.audio_to_speech(audio))