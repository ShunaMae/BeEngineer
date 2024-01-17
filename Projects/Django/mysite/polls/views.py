from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request, keyword):
    context = {"msg": "Please vote.",
            "keyword": keyword}
    return render(request, "polls/index.html", context)

