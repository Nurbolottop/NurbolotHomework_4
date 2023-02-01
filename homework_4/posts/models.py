from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="post_comment", verbose_name="Пост")
    name = models.CharField(max_length=255,verbose_name="Имя автора")
    text = models.CharField(max_length=255,verbose_name="Текс комментария")
    created = models.DateField(auto_now=True, verbose_name="Дата создания")
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"