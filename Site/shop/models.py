from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    """Model representing user profile information."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=False)
    location = models.CharField(max_length=30, blank=False)
    birth_date = models.DateField(null=True, blank=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    role_at_shop = models.CharField(max_length=50, blank=False, null=False)
    owner_of_shop = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    email_address = models.EmailField(max_length=255, blank=False, null=False)
    shop_description = models.TextField(blank=True, null=True)
    date_of_joining = models.DateField(default=timezone.now)
    subscription_detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class ThreeDModel(models.Model):
    """Model representing a 3D model associated with a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='models')
    model_id = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    description = models.TextField()
    obj_file = models.FileField(upload_to='models/', blank=True, null=True)  # Add this line

    def __str__(self):
        return f'{self.model_id} - {self.user.username}'
