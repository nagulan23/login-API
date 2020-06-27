from django.db import models
from django.utils import timezone

class User(models.Model):
    
    def number():
        if User.objects.count()==0:
            return 0
        no = getattr(User.objects.latest('uid'),'uid')
        if no == None:
            return 1
        else:
            return no + 1
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = timezone.now()
        self.modified_time = timezone.now()
        return super(User, self).save(*args, **kwargs)
    
    uid=models.IntegerField(default=number)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=60,unique=True)
    password=models.CharField(max_length=60)
    mobile_number=models.CharField(max_length=15)
    address=models.CharField(max_length=99999,default="null",auto_created=True,)
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    
    def __str__(self):
        return self.name