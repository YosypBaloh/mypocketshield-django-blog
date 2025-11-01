from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField('A cikk neve', max_length=100, unique=True, default='Új cikk')
    text = models.TextField('A cikk szövege')
    date = models.DateTimeField('Dátum',default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Szerző', on_delete=models.CASCADE)

    views = models.IntegerField('Megtekintések', default=1)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Hír'
        verbose_name_plural = 'Hírek'