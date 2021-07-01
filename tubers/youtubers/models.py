from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):

    CREW_CHOICES = (
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    CAMERA_CHOICE = (
        ('canon','canon'),
        ('nikon','nikon'),
        ('sony','sony'),
        ('red','red'),
        ('fuji','fuji'),
        ('panasonic','panasonic'),
        ('other','other')
    )

    CATEGORY_CHOICES = (
        ('code','code'),
        ('mobile_review','mobile_review'),
        ('vlogs','vlogs'),
        ('comedy','comedy'),
        ('gaming','gaming'),
        ('film_making','film_making'),
        ('cooking','cooking')
    )

    name = models.CharField(max_length = 255)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="media/ytubers/%Y%m")
    video_url = models.CharField(max_length = 255)
    description = RichTextField()
    city = models.CharField(max_length = 255)
    age = models.IntegerField(default=18)
    height = models.IntegerField()
    crew = models.CharField(max_length = 255,choices = CREW_CHOICES)
    camera_type = models.CharField(max_length = 255,choices = CAMERA_CHOICE)
    subs_count = models.IntegerField()
    category = models.CharField(max_length = 255,choices = CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
