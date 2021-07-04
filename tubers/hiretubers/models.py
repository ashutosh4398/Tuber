from django.db import models

# Create your models here.
class HireTuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    state = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
