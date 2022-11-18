from django.http import request

from .models import Profile


def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.image
        return {'picture_profile': pic}
    return {}

