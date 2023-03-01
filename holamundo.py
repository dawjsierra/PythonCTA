from gtts import gTTS
import os

mytext = 'TWENTY-ELEVEN'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("2011.mp3")
os.system("2011.mp3")