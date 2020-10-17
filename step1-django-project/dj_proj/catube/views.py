from django.shortcuts import render
from .models import Video


def video_list(request):
    qs = Video.objects.all()  # QuerySet 객체
    # catube/templates/catube/video_list.html
    return render(request, 'catube/video_list.html', {
        'video_list': qs,
    })
