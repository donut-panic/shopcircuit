from PIL import Image
from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, CharField, TextField, ImageField
from tinymce.models import HTMLField

GENDER = (('male' , 'Male'),
              ('female', 'Female'),
              ('other', 'Other'))

class Profile(Model):

    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(upload_to='accounts/static/images', blank=True, null=True)
    gender = CharField(max_length=6, choices=GENDER, default='Male', blank=True)
    biography = HTMLField(blank=True)


    def __str__(self):
        return f"{self.user.username} Profile"
