
from gtts import gTTS
text = "안녕"
tts = gTTS(text=text, lang='ko')
filename = "voice.mp3"
tts.save(filename)



