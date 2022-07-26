

from django.db import models
#DataFlair Models
class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default=0)
    email = models.EmailField(blank = True)
    describe = models.TextField(default = "DataFlair Django tutorials")
    def __str__(self):
        return self.name

class Category(models.Model):
    id= models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=255)
    cat_slug = models.CharField(max_length=255)
    # status = models.CharField(max_length=30, default=1)
    status = models.BooleanField()
    def __str__(self):
        return self.cat_name