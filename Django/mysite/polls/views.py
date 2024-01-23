from django.shortcuts import render


def index(request):
    question_list = [
        "Do you like programming?",
        "Do you like math?",
        "Do you like Japanese?",
    ]

    context = {
        "question_list": question_list,
        "is_polled": True,
        "polled_msg": "Thank you for voting.",
        "not_polled_msg": "You haven't voted yet",

    }

    return render(request, "polls/index.html", context)

def result(request):
    question_dict = {
        "Do you like programming?": True,
        "Do you like math?" : True,
        "Do you like Japanese?" : True
        }
    
    context = {
        "question_dict": question_dict
    }

    return render(request, "polls/result.html", context)
