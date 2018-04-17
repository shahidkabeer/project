import sounddevice as sd
import soundfile as sf
import threading
from threading import Thread

def audioFunc1():
    audio1 = "_Rear_Left.wav"
    data1, fs1 = sf.read(audio1, dtype='float32')
    sd.play(data1, fs1, device=7)   #Rear_Left
    while(1):
	a=10

def audioFunc2():
    audio2 = "_Rear_Right.wav"
    data2, fs2 = sf.read(audio2, dtype='float32')
    sd.play(data2, fs2, device=8)  #Rear_Right
    while(1):
	a=10

def audioFunc3():
    audio2 = "_Center.wav"
    data2, fs2 = sf.read(audio2, dtype='float32')
    sd.play(data2, fs2, device=6)  #Center
    while(1):
	a=10
def audioFunc4():
    audio2 = "_Front_Left.wav"
    data2, fs2 = sf.read(audio2, dtype='float32')
    sd.play(data2, fs2, device=4)  #Front_Left
    while(1):
	a=10
def audioFunc5():
    audio2 = "_Front_Right.wav"
    data2, fs2 = sf.read(audio2, dtype='float32')
    sd.play(data2, fs2, device=5)  #Front_Right
    while(1):
	a=10


t1 = threading.Thread(target=audioFunc1, args=[])
t1.start()
t2 = threading.Thread(target=audioFunc2, args=[])
t2.start()
t3 = threading.Thread(target=audioFunc3, args=[])
t3.start()
t4 = threading.Thread(target=audioFunc4, args=[])
t4.start()
t5 = threading.Thread(target=audioFunc5, args=[])
t5.start()

