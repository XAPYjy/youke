from django.shortcuts import render


# Create your views here.

def video_view(request, video_url):
    return render(request, "video_rtmp/index.html", locals())
