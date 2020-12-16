
from gtts import gTTS
import os
fp=open('New Text Document.txt','r')
mytext=fp.read().replace('\n',' ')
language='bn'
output=gTTS(text=mytext,lang=language,slow=False)
output.save('output.mp3')
fp.close()
os.system('start output.mp3')



