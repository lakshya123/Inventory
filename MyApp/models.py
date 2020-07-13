from django.db import models

class Book(models.Model):
    ISBN = models.CharField(max_length = 13,blank = True)
    Title = models.CharField(max_length = 100,blank = True)
    Subject = models.CharField(max_length = 30,blank = True)
    Author = models.CharField(max_length = 20,blank = True)
    Language = models.CharField(max_length = 10,blank = True)
    Stock = models.IntegerField(blank = True)
    TimeStamp = models.DateField(auto_now_add= True)

    def __unicode__(self):
        return self.Title
