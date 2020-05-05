from django.db import models

# Create your models here.

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=50,verbose_name="Dersin İsmi")
    
    def __str__(self):
        return str(self.lesson_name)

class Book(models.Model):
    lesson_name = models.ForeignKey(Lesson,on_delete=models.CASCADE,verbose_name="Dersin İsmi")
    book_name = models.CharField(max_length=50,verbose_name="Kitabın İsmi",null=True)
    author = models.CharField(max_length=50,verbose_name="Yazar")
    page_count = models.IntegerField(verbose_name="Sayfa Sayısı")

    def __str__(self):
        return str(self.book_name) if str(self.book_name) else ""

class Topic(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,verbose_name="Kitabın İsmi")
    topic_name = models.CharField(max_length=50,verbose_name="Konu İsmi")

    def __str__(self):
        return str(self.topic_name)    

class Homework(models.Model):
    student = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Öğrenci İsmi")
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,verbose_name="Ders")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,verbose_name="Kitap")
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,verbose_name="Konu")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulan Zaman")
    initial_date = models.DateField(verbose_name="Başlangıç Vakti")
    final_date = models.DateField(verbose_name="Bitiş Vakti")
    total_solved = models.IntegerField(verbose_name="Toplam Çözülen Soru",null=True,default=0,blank = True)
    true_solved = models.IntegerField(verbose_name="Doğru Çözülen Soru Sayısı",null=True,default=0,blank = True)
    false_solved = models.IntegerField(verbose_name="Yanlış Çözülen Soru Sayısı",null=True,default=0,blank = True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created_date']

