from django.shortcuts import render


def play_video(request,video_url):
    return render(request, "lesson_mgr/play_video.html", locals())
