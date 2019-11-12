from django.contrib.auth.models import User
from .models import Wish
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_wish(sender, instance, created, **kwards):
	if created:
		Wish.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_wish(sender, instance, **kwards):
	instance.wish.save()