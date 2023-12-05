from django.db import models

class Yacht(models.Model):
    yid= models.CharField(max_length=50,null=False,default=1)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    yachtPhoto =models.ImageField(upload_to='photos/%y/%m/%d')
    
    class Meta:
        verbose_name = "Yacht"

    def __str__(self):
        return self.title

