from django.db import models


class User(models.Model):
    user_id = models.IntegerField()
    nickname = models.TextField('NickName')
    login = models.TextField()
    password = models.TextField()

    def __str__(self) -> str:
        return self.login
    

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"