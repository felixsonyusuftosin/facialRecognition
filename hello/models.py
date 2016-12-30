from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class face(models.Model):
    pictures= models.ManyToManyField('piclist')
    account = models.CharField(max_length = 10,null= True, blank = True)  
    Time = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return '%s'% self.Time
class piclist(models.Model):
    Picture  = models.ImageField(upload_to = 'piclist/%Y/%m/%d',blank = True, null = True)
    Time = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return '%s'% self.Time
    class Meta:
        verbose_name = 'Pictures mobile'

