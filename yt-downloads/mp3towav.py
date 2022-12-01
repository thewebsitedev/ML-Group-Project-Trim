from pydub import AudioSegment
import os

sc_list = os.listdir( 'podcasts-portion' )
# print(sc_list)

i = 1

for file in sc_list:
    if file.endswith(".mp3") :
        #importing file from location by giving its path
        sound = AudioSegment.from_mp3("podcasts-portion/"+file)
        sound = sound.set_channels(1)

        name = file.split(".mp3")
        sound.export("wav-mono/"+name[0]+".wav", format="wav")

        print( "{} audio trimmed: ".format(i, 1) + name[0] + ".wav" )

        i += 1