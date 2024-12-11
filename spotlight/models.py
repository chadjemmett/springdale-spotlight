from django.db import models

# Create your models here.

class Winner(models.Model):
    
    paragraph = models.TextField(blank=False)
    
    winner_name = models.CharField("Winner's Name", max_length=255)

    social_media_url = models.CharField("Social Media Link", max_length=255)

    image_1 = models.CharField("Image 1", max_length=255)
    image_2 = models.CharField("Image 2", max_length=255)
    image_3 = models.CharField("Image 3", max_length=255)
    
    alt_text_1 = models.CharField("Alt Text 1", max_length=255)
    alt_text_2 = models.CharField("Alt Text 2", max_length=255)
    alt_text_3 = models.CharField("Alt Text 3", max_length=255)
    
    headline = models.CharField("Headline", max_length=255)

   
    def __str__(self):
        return self.winner_name
