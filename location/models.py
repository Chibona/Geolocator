
from django.db import models

class Location(models.Model):
    ip_address = models.CharField(max_length=45)  # Accommodates both IPv4 and IPv6
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    isp = models.CharField(max_length=100)
    lan = models.CharField(max_length=100)
    lon = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}, {self.country} ({self.ip_address})"
