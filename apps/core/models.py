from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from PIL import Image

from apps.home.models import Cabang

class AccountsUser(AbstractUser):
    email = models.EmailField(_('email address'),unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar", blank= True)

    is_banned = models.BooleanField(default=False)
    jumlah_banned = models.IntegerField(blank=True, null=True, default=0)
    cabang = models.ForeignKey(Cabang, null=True, blank=True,related_name='val_cab',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.avatar.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (250, 250)
            img.thumbnail(output_size) # Resize image
            img.save(self.avatar.path)

class Visitor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, related_name='visitor', on_delete=models.CASCADE)
    session_key = models.CharField(null=False, max_length=40)

    class Meta:
        db_table = 'visitor'