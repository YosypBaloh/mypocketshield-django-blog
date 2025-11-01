from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Felhasználó"
    
    )
    img = models.ImageField('Profilkép', 
        default='user_profileimages/default.png', 
        upload_to='user_profileimages')

    def __str__(self):
        return f'Felhasználói profil {self.user.username}'
    
    def save(self, *args, **kwargs):
       super().save()

       image = Image.open(self.img.path)

       if image.height > 256 or image.width > 256:
          resize = (256, 256)
          image.thumbnail(resize)
          image.save(self.img.path)
    
    class Meta:
      verbose_name = 'Profil'
      verbose_name_plural = 'Profilok'