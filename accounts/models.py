from PIL import Image
from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, CharField, TextField, ImageField
from tinymce.models import HTMLField


class Profile(Model):
    GENDER = [('M' , 'Male'),
              ('F', 'Female'),
              ('O', 'Other')
              ]

    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(upload_to='accounts/static/images', blank=True, null=True)
    gender = CharField(max_length=6, choices=GENDER, default='M', blank=True)
    biography = HTMLField(blank=True)


    def __str__(self):
        return f"{self.user.username} Profile"
