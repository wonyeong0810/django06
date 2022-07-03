from webbrowser import Konqueror
from django.shortcuts import render
from googletrans import Translator
import googletrans
# Create your views here.
def index(request):
    context = {
        "ndict" : googletrans.LANGUAGES
    }
    if request.method == "POST":
        t1 = request.POST.get("trans1")
        t2 = request.POST.get("trans2")
        tw = request.POST.get("transw")
        translator = Translator()
        trans = translator.translate(tw, src=t1, dest=t2)
        t = trans.text
        context.update({
            "t" : t,
            "tt" : tw,
            "t1" : t1,
            "t2" : t2
        })
    
    return render(request, "trans/index.html", context)
