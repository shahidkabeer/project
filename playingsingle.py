import sounddevice as sd
import soundfile as sf
import threading
from threading import Thread

def audioFunc1():
    audio1 = "audio1.wav"
    data1, fs1 = sf.read(audio1, dtype='float32')
    sd.play(data1, fs1, device=7)   #speakers

def audioFunc2():
    audio2 = "audio1.wav"
    data2, fs2 = sf.read(audio2, dtype='float32')
    sd.play(data2, fs2, device=5)  #headset

if __name__ == '__main__':
    Thread(target = audioFunc1).start()
    #Thread(target = audioFunc2).start()
