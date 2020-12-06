from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Project(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



