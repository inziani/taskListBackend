from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



from .models import User, UserProfile
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.userProfile.save()