from django.contrib import admin
from .models import Announcement

# Register your models here.

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["title","created_date","announcement_file","youtube"]

    search_fields = ["title"]

    list_filter = ["created_date","title"]

    class Meta:
        model = Announcement

