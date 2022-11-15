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
    image = ImageField(upload_to='accounts/static/images', default="default.jpg", blank=True, null=True)
    gender = CharField(max_length=6, choices=GENDER, default='M', blank=True)
    biography = HTMLField(blank=True)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     super(Profile, self).save()
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __str__(self):
        return f"{self.user.username} Profile"
