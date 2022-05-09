from django.db import models

class DigitalProduct(models.Model):
    name=models.TextField()
    file=models.FileField(upload_to='products/')

    def __str__(self):
        if len(self.name)>=50:
            return f"{self.name[50]}..."
        else:
            return self.name

    class Meta:
        verbose_name_plural='Digital Products'