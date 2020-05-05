from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Announcement(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Oluşturulan Zaman")
    announcement_file = models.FileField(
        blank=True, null=True, verbose_name="Duyuruya Dosya Ekleyin")
    youtube = models.URLField(
        verbose_name="Youtube URL si Giriniz", null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created_date']
