from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catube import views

urlpatterns = [
    path('djadmin/', admin.site.urls),
    path('', views.video_list),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
