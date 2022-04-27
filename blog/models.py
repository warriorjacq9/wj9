from django.db import models

# Create your models here.
class Post(models.Model):
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    name=models.TextField()

    class Meta:
        verbose_name_plural='Blog Posts'
    
    def __str__(self):
        if len(self.text)>=50:
            return f"{self.text[50]}..."
        else:
            return f"{self.text}"

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Comments'
    
    def __str__(self):
        if len(self.text)>=50:
            return f"{self.text}..."
        else:
            return self.text