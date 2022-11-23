"""from vosk import Model, KaldiRecognizer
import pyaudio
import json

#import os
#os.listdir('../System/widgests/model')

model = Model('model')
rec = KaldiRecognizer(model, 14000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()
cont = 0
while True:
    data = stream.read(8000)
    if len(data) == 0 or cont == 7:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        if result is not None:
            text = result['text']
            print(text)
        cont += 1"""

import speech_recognition as sr

# cria um reconhecedor
r = sr.Recognizer()

# ABRIR MICRO PARA CAPTURAR
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)  # define micro fone com fonte de audio
        print(r.recognize_google(audio))