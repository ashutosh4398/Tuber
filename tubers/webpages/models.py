from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/slider/%Y/")
    created_date = models.DateTimeField(auto_now_add=True)
    redirect_to = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.headline}"
