from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    # В файле models.py нашего приложения создаём модель Phone с полями id, name, price,
    # image, release_date, lte_exists и slug. Поле id — должно быть основным ключом модели.
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_data = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True)
