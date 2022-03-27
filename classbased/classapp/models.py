from django.db import models
from django.urls import reverse
# Create your models here.
class Musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name+' '+self.last_name
    def get_absolute_url(self):#in order to submit the form
        return reverse('classapp:musician_detail',kwargs={'pk':self.pk})

class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE,related_name='album_list')#related_name for showing albums into musician_detail.html
    name=models.CharField(max_length=50)
    release_date=models.DateField()
    rating=(
    (1,'worst'),
    (2,'bad'),
    (3,"not bad"),
    (4,'good'),
    (5,'Excellent'),
    )
    num_stars=models.IntegerField(choices=rating)

    #class Meta:
        #db_table='album'


    def __str__(self):
        return self.name
