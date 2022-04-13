from django.db import models


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    comment = models.CharField(max_length=255)

# Создание файл инструкцию по внесенным измениям
# python manage.py makemigrations

# Реализация изменений согласно созданных инструкций
# python manage.py migrate

    def __str__(self):
        return f"{self.pk}, {self.firstname}"

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"