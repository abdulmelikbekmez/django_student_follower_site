from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Homework,Lesson,Book,Topic

# Register your models here.
@admin.register(Homework)
class HomeworkAdmin(ImportExportModelAdmin):
    list_display = ["student","title","lesson","initial_date","final_date"]

    search_fields = ["title"]

    list_filter = ["student","title","initial_date","final_date"]


    class Meta:
        model = Homework

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    class Meta:
        model = Lesson




admin.site.register(Book)


admin.site.register(Topic)

 
