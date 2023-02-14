from gtts import gTTS
import os















mytext = 'SANCHEZ QUE TE VOTE CHAPOTE, ROJO DE MIERDA'
language = 'es'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("perrosanxe.mp3")
os.system("mpg321 perrosanxe.mp3")