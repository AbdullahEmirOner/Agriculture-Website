from django.db import models



class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)  # Son güncelleme tarihi

    def __str__(self):
        return f"{self.city} - {self.temperature}°C"
    
class AgricultureNews(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField()
    url = models.URLField()
    image_url = models.URLField(blank=True, null=True)  # Resim URL'si için boş geçilebilir

    def __str__(self):
        return self.title
