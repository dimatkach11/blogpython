from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    publish = models.BooleanField(default=False)
    data_pubblicazione = models.DateField(blank=True, null=True)
    
    #mi definisce come verra visualizzato il mio posto, che nome avra
    def __str__(self):
        return f'{self.pk}:{self.title}'

    class Meta:
        verbose_name = 'Articolo'
        verbose_name_plural = 'Articoli'
        ordering = ('data_pubblicazione',)