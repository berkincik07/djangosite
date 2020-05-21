from django.db import models
from ckeditor.fields import RichTextField
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=True,verbose_name = "Yazar")
    title = models.CharField(max_length=60,verbose_name="Başlık")
    content = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.ImageField(blank = True,null = True,verbose_name = "Makalenize Fotoğraf Ekleyin (isteğe bağlı)")
# Create your models here.

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['-created_time']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length=25,verbose_name="İsim")
    comment_content = models.CharField(max_length=100,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta():
        ordering = ['-comment_date']
