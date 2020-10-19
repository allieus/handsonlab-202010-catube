from django.views.generic import ListView
from django.shortcuts import render
from .models import Video


# def video_list(request):
#     qs = Video.objects.all()  # QuerySet 객체
#     # catube/templates/catube/video_list.html
#     return render(request, 'catube/video_list.html', {
#         'video_list': qs,
#     })

# 함수를 만들어준다.
video_list = ListView.as_view(model=Video, paginate_by=2)
