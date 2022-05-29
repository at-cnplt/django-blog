from django.db import models
from ckeditor.fields import RichTextField

import article

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=50,verbose_name= "Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye bir fotoğraf ekleyin")


    def __str__(self) -> str:
        return self.title
        
    class Meta():
        ordering = ['-created_date']



class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete= models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="yorum")
    comment_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.comment_content
    
    class Meta():
        ordering = ['-comment_date']
