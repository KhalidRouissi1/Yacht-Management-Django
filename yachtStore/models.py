from django.db import models

class Yacht(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    yachtPhoto = models.ImageField(default='media/default.jpg')  
    

    class Meta:
        verbose_name = "Yacht"

    def __str__(self):
        return self.title

