import os
import shutil
path= '/home/shahidkabeer/music/src/music'
files = os.listdir(path)
i = 'audio'

for file in files:
	f=file
	ex=f.split(".")[-1]
	if ex == 'mp3':    
		os.rename(os.path.join(path, file), os.path.join(path, i+'.mp3'))
		os.system('sox /home/shahidkabeer/music/src/music/audio.mp3 /home/shahidkabeer/music/src/music/mixer_input.wav')

shutil.move("/home/shahidkabeer/music/src/music/mixer_input.wav", "/home/shahidkabeer/music/src/mixer_input.wav")
