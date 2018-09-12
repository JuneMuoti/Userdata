from django.db import models



class User(models.Model):
    Name=models.CharField(max_length=60)
    Location=models.CharField(max_length=60)
    Age=models.IntegerField()
    email=models.EmailField()


    def __str_(self):
        return self.Name
