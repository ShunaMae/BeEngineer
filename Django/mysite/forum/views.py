from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Message

# Create your views here.

def index(request):
    topic_list = Topic.objects.all()
    context = {
        "topic_list": topic_list,
    }
    return render(request, "forum/index.html", context)


def forum(request, topic):
    topic_obj = Topic.objects.get(name=topic)
    print(topic_obj)
    msgs= Message.objects.filter(topic=topic_obj).order_by("created_at")
    

    new_message = request.POST['tweet']
    print(new_message)
    message = Message.objects.create(topic=topic_obj, content=new_message)
    print(message)
    # return redirect('forum:forum', topic=topic_obj.name)


        

    context = {
        "topic": topic_obj,
        "messages": msgs
    }

    return render(request, "forum/forum.html", context)





