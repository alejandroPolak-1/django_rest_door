from django.db import models

# Create your models here.

class Personal(models.Model):
    email       = models.EmailField(max_length=255, unique=True)
    name        = models.CharField(max_length=255)
    lastname    = models.CharField(max_length=255)
    dni         = models.CharField(max_length=30)
    doors       = models.ManyToManyField('Door', through='PersonalByDoors')
    movil_user  = models.BooleanField(default=False)
    
        
    def __str__(self):
        # return "%s %s" % (self.name, self.users)
        return str(self.id) + '-' + self.email

    
class Door(models.Model):
    id         = models.AutoField(primary_key=True) 
    name       = models.CharField(max_length=255, unique=True)
    hash       = models.CharField(max_length=100)
    personals  = models.ManyToManyField('Personal', through='PersonalByDoors')
      
   
    def __str__(self):
        # return "%s %s" % (self.name, self.users)
        return self.name   
    
class PersonalByDoors(models.Model):
    personal  = models.ForeignKey(Personal, on_delete=models.CASCADE)
    door  = models.ForeignKey(Door, on_delete=models.CASCADE)
    
    
    class Meta:
        unique_together = [['personal', 'door']]
        
    def __str__(self):
            # return "%s %s" % (self.name, self.users)
       return "%s %s" % (self.door, self.personal)