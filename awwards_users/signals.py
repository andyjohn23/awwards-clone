from django.db.models.signals import post_save
from django.dispatch import receiver
from awwards_users.models import Profile, UserAccount

@receiver(post_save, sender=UserAccount)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=UserAccount)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()