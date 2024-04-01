from django.db import models
from core.models import Appeal
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='course_videos/')  # For video file uploads
    ratings = models.FloatField(default=0.0)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class Blogs(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    blog_img=models.ImageField(upload_to='blog_img/')
    appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField()
    
    def __str__(self):
	    return f" title : {self.title}"
    class Meta:
        ordering = ['-created_date']

class Gift(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    gift_img=models.ImageField(upload_to='gift_img/')
    def __str__(self):
	    return f" name : {self.name}"

class OurWork(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    work_img=models.ImageField(upload_to='work_image/')
    created_date = models.DateTimeField()
    
    def __str__(self):
	    return f" title : {self.title}"

    class Meta:
        ordering = ['-created_date']

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

class GiftSold(models.Model):
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.gift.name}"
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name     
