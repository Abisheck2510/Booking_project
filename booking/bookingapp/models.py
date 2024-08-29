from django.db import models

class Booking(models.Model):
    SERVICE_CLASSES = [
        ('seater', 'Seater'), 
        ('semi-sleeper', 'Semi-Sleeper'), 
        ('sleeper', 'Sleeper')
    ]

    GENDER_CLASSES = [
        ('male','Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]

    passenger_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=20, choices=GENDER_CLASSES, default=None)
    phone_number = models.CharField(max_length=100, null=False, blank=False)
    pickup_point = models.CharField(max_length=30)
    drop_point = models.CharField(max_length=30)
    service_class = models.CharField(max_length=20, choices=SERVICE_CLASSES, default='seater')

    def __str__(self):
        return f"{self.passenger_name} - {self.service_class}"
