from django.db import models


class Article(models.Model):
    # Статья, к которой крепятся комментарии
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Комментарий.
    Поле pid равно id родительского комментария.
    Поле depth, если оно отрицательно, указывает на уровень вложенности (-3 - комментарий первого уровня,
    -2 - второго, -1 - третьего); в противном случае указывает на id родительского комментария третьего уровня.
    Сортировка по полю pid позволяет нам построить древовидную структуру комментариев.
    Ограничение по полю depth < 0 дает возможность выдавать комментарии только до третьего уровня,
    с их последующим раскрытием по запросу depth = n, для n > 0.
    """
    article = models.ForeignKey(Article, related_name='comment_content', on_delete=models.CASCADE)
    pid = models.IntegerField(default=0)
    depth = models.IntegerField(default=-3)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pid', 'id']

    def __str__(self):
        return self.timestamp

    def save(self, *args, **kwargs):
        try:
            parents_depth = Comment.objects.get(id=self.pid).depth
        except models.ObjectDoesNotExist:
            self.depth = -3
        else:
            if parents_depth < -1:
                self.depth = parents_depth + 1
            elif parents_depth == -1:
                self.depth = self.pid
            else:
                self.depth = parents_depth
        super(Comment, self).save(*args, **kwargs)

    def delete(self):
        # Перегружаем метод delete, чтобы не ломать дерево вложенности при удалении комментария
        self.content = "Комментарий удален"
