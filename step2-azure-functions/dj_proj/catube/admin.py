from django.contrib import admin
from .models import Video
from .forms import VideoForm


class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    form = VideoForm

admin.site.register(Video, VideoAdmin)
