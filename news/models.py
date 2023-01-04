from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class news(models.Model):
    numbercard = models.CharField(max_length=2)
    title = models.CharField(max_length=200)
    description =models.TextField(max_length=3000)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    date = models.DateTimeField(null=True)
    timing = models.DateField(auto_now=False)
    slug = models.CharField(max_length=1000, null=True , blank=True)
    subDiscribtion = models.TextField(max_length=3000)
    

    def save(self,*args , **kwargs):
        if not self.slug:
            self.slug= slugify(self.numbercard + "-" + str(self.timing))

        return super().save(*args , **kwargs)   
