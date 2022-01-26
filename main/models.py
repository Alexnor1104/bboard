from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Сделать оповещения о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass


# Базовая модель рубрик
class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Название')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Порядок')
    super_rubric = models.ForeignKey('SuperRubric', on_delete=models.PROTECT,
                                     null=True, blank=True, verbose_name='Надрубрика')
