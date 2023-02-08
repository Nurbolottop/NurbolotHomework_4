from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    status = models.BooleanField(default=True, verbose_name="Статус публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment", verbose_name="Пост")
    name = models.CharField(max_length=16, verbose_name="Имя автора")
    text = models.CharField(max_length=300, verbose_name="Текст комментария")
    created = models.DateTimeField(auto_now=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.post.title} - {self.name}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
