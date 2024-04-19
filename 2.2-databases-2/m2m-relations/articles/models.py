from django.db import models


class Tag(models.Model): # просто тег, только его название, ничего более;
    name = models.CharField(max_length=256, verbose_name='Название тега')


class Article(models.Model): # статья с текстом, заголовком, картинкой и пр. + набор тегов (многие ко многим);

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField('Tag', through='Scope', blank=True, verbose_name='Раздел', related_name='tags')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model): # таблица-связка между статьей и тегом. Именно здесь должно быть свойство is_main
    is_main = models.BooleanField(verbose_name="Основной", default=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
