from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save


# Create your models here.


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images',blank=True, null=True)
    bio = models.TextField()
    PRDSlug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})

def handle_user_creation(sender,**kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

        
        
        
post_save.connect(handle_user_creation,sender=User)        
