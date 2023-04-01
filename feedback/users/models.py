from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQPNCrd8ZQ-UEFCbmPpPLhu81cTgDtzHhoHX9htAzri8iwSpCKI"
class CostomUser(AbstractUser):
    role = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='media', default='media/0.png')
    bio = models.TextField()
    user_qr =  models.ImageField(upload_to='qr_store', blank=True)
