from django.db import models

from django.core.validators import MinValueValidator

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    fees = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='course_category')
    
    def __str__(self):
        return self.title
    
    