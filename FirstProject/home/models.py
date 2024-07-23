from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    #image = models.ImageField()
    #file = models.FileField()

    def __str__(self) -> str:
        return self.name


#Comments:
#Django at the time of running runs all the migrations present and creates a stateand check with that present in the database 

