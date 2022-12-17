from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, CharField, ImageField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    first_name = CharField(max_length=255, null=True, blank=True, default="")
    last_name = CharField(max_length=255, null=True, blank=True, default="")
    phone = CharField(max_length=30, null=True, blank=True, default="")
    street = CharField(max_length=255, null=True, blank=True, default="")
    house = CharField(max_length=255, null=True, blank=True, default="")
    city = CharField(max_length=255, null=True, blank=True, default="")
    postal_code = CharField(max_length=255, null=True, blank=True, default="")
    image = ImageField(upload_to="accounts/static/images", null=True, blank=True)


    def __str__(self):
        return self.user.username
