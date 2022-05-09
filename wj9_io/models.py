from django.db import models

class DigitalProduct(models.Model):
    name=models.TextField()
    file=models.FileField(upload_to='products/')

    class Meta:
        verbose_name_plural='Digital Products'