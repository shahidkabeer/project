import sounddevice as sd
import soundfile as sf
import threading
from threading import Thread

def audioFunc1():
    audio1 = "_Rear_Left.wav"
    data1, fs1 = sf.read(audio1, dtype='float32')
    sd.play(data1, fs1, device=7)   #speakers
     while(1):
	a=10

def audioFunc2():
    audio2 = "_Center.wav"
    data2, fs2 = sf.read(audio2, dtype='float32')
    sd.play(data2, fs2, device=5)  #headset
    while(1):
	a=10


t1 = threading.Thread(target=audioFunc1, args=[])
t1.start()
t2 = threading.Thread(target=audioFunc2, args=[])
t2.start()


