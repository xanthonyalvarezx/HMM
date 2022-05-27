from django.db import models

# Create your models here.
# Model to create an admin
class Register(models.Model):
  name = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  age = models.IntegerField()
  email = models.EmailField(max_length=254)

  def _str_(self):
    return self.name



