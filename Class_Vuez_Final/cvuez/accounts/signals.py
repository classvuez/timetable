from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import UserProfile, Lecturer, Student, Administrator


def user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(auth_user=instance)
        print('Profile created!')


post_save.connect(user_profile, sender=User)

"""
def lecturer(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Lecturer')
        instance.groups.add(group)

        Lecturer.objects.create(auth_user=instance)
        print('Lecturer added!')


post_save.connect(lecturer, sender=User)


def student(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Student')
        instance.groups.add(group)

        Student.objects.create(auth_user=instance)
        print('Student added!')


post_save.connect(student, sender=User)


def administrator(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Admin')
        instance.groups.add(group)

        Administrator.objects.create(auth_user=instance)
        print('Administrator added!')


post_save.connect(administrator, sender=User)"""


