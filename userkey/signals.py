from django.contrib.auth.models import User
from .models import UserKey
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.core.exceptions import PermissionDenied

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        from Crypto.PublicKey import RSA
        from Crypto import Random
        random_generator = Random.new().read
        key = RSA.generate(1024, random_generator)
        UserKey.objects.create(user=instance,
         public_key=key.publickey().exportKey(),
         private_key=key.exportKey())

post_save.connect(create_user_profile, sender=User)

@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    if instance.is_superuser:
        raise PermissionDenied
