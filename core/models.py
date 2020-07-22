from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# TODO separete in a service, a publisher dashboard
class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    publication_year = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='games')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='games')
    price = models.DecimalField(max_digits=12, decimal_places=2)
