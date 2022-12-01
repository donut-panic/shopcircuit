from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from store.models import Wishlist


@receiver(post_save, sender=User)
def create_wishlist(sender, instance, created, **kwargs):
    if created:
        Wishlist.objects.create(user=instance, products='{"products":[]}')


@receiver(post_save, sender=User)
def create_wishlist(sender, instance, **kwargs):
    instance.wishlist.save()