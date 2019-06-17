# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from blogapp.models import Profile
# from django.contrib.auth.models import User


# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile=Profile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile ,sender=User)

# @receiver(post_save , sender=User)
# def create_user_profile(sender , instance ,  created , **kwargs):
#     print("under create")
#     if created and not instance.is_staff:
#         # attrs_needed = ['_otherfield',]
#         print(kwargs)
#
#         # if all(hasattr(instance, attr) for attr in attrs_needed):
#         print("hello2")
#         Profile.objects.create(user=instance)  #, phone=instance._otherfield
#         print("hello3")
#         instance.profile.save()
#         print("hello1")

# @receiver(post_save , sender=User)
# def save_user_profile(sender , instance , **kwargs):
#     print(instance)
#     if not instance.is_staff:
#         print("profile save")
#         instance.profile.save()
#         print("hello2")

# post_save.connect(create_user_profile, sender=User, weak=False)
