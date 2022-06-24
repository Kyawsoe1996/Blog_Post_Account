from django.db import models


# Create your models here.

class Industry(models.Model):
    name=models.TextField()

    def __str__(self):
        return self.name
    


class Job(models.Model):
    title = models.TextField()
    industry = models.ForeignKey(to=Industry,related_name="jobs",on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Person(models.Model):
    name = models.TextField()
    age = models.PositiveSmallIntegerField()
    job = models.ForeignKey(to=Job, related_name="persons",on_delete=models.CASCADE)
   


    def __str__(self):
        return self.name
    