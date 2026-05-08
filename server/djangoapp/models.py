from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealerID = models.CharField(max_length=50, null=True, blank=True)
    #dealerID = models.IntegerField()
    name = models.CharField(max_length=30)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2026,
        validators = [
            MaxValueValidator(2026),
            MinValueValidator(2015)
        ]
    )
    
    def __str__(self):
        return self.name
