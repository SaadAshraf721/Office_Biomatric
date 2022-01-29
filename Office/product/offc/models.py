from django.db import models
import datetime
# Create your models here.


class ofice(models.Model):

    nam = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    level = models.IntegerField()
    create_at = models.DateTimeField(auto_now=True)

class department(models.Model):
    name = models.CharField(max_length = 50)
    create_at = models.DateTimeField(auto_now=True)

class adoo(models.Model):
    oi= models.ForeignKey(ofice, on_delete=models.CASCADE)
    di= models.ForeignKey(department, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)


# class ao(models.Model):
#     aoa= models.ForeignKey(office, on_delete=models.CASCADE)
#     aob= models.ForeignKey(office, on_delete=models.CASCADE)

# class ai(models.Model):
#     aia= models.ForeignKey(office, on_delete=models.CASCADE)
#     aib= models.ForeignKey(office, on_delete=models.CASCADE)    
