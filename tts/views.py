from django.shortcuts import render
from gtts import gTTS
# Create your views here.
def index(request):
    context = {
        
    }
    if request.method == "POST":
        t = request.POST.get("text")
        tts = request.POST.get("tts")
        mp3 = request.POST.get("mp3")
        tt = gTTS(text=t, lang=tts)
        filename = f"media/{mp3}.mp3"
        tt.save(filename)
        context = {
            "tts" : mp3,
            "text" : t
        }
    return render(request, "tts/index.html", context)