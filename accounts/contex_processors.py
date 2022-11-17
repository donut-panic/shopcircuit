from django.http import request

from .models import Profile


def profile_pic(reguest):
    if reguest.user.is_authenticated:
        profile_obj = Profile.objects.get(user=reguest.user)
        pic = profile_obj.image
        return {'picture_profile': pic}
    return {}

