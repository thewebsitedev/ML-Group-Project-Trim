from pydub import AudioSegment
import os

sc_list = os.listdir( 'soundcloud' )
# print(sc_list)

for file in sc_list:
    if file.endswith(".mp3") :
        #importing file from location by giving its path
        sound = AudioSegment.from_mp3("soundcloud/"+file)

        #Selecting Portion we want to cut
        StrtMin = 0
        StrtSec = 75

        EndMin = 0
        EndSec = 90

        # Time to milliseconds conversion
        StrtTime = StrtMin*60*1000+StrtSec*1000
        EndTime = StrtMin*60*1000+EndSec*1000

        # Opening file and extracting portion of it
        extract = sound[StrtTime:EndTime]

        # Saving file in required location
        extract.export("soundcloud-portions/"+file, format="mp3")

        print( "audio trimmed: " + file )

        # new file portion.mp3 is saved at required location