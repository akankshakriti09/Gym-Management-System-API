from django.db import models

# Create your models here.
class Gym(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name_plural = 'Gym'

class Trainer(models.Model):
    Name = models.CharField(max_length=100)
    Specialization = models.CharField(max_length=100)
    Gym = models.OneToOneField(Gym, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name   
    
    class Meta:
        verbose_name_plural = 'Trainer'

class Client(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Client'

class WorkoutSession(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    Date = models.DateField(auto_now=False,auto_now_add=False)
    Duration = models.IntegerField()

    def __str__(self):
        return self.Duration

    class Meta:
        verbose_name_plural = 'WorkoutSession'
        
       




