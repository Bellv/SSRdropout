from django.db import models


class Member(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    description = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    gb_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    gb_id = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )

    GB_GENDER_CHOICE = (
        ('gran', 'Gran'),
        ('deeja', 'Deeja'),
    )

    gb_gender = models.CharField(
        max_length=20,
        choices=GB_GENDER_CHOICE,
        default='gran'
    )

    gb_class = models.CharField(
        max_length=20,
        default='fighter'
    )

    gb_waifu = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    facebook = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    twitter = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    discord = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    STATUS_CHOICE = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        default='active'
    )

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )

    GB_CATAGORY_CHOICE = (
        ('gbclass', 'Class'),
        ('character', 'Character'),
        ('weapon', 'Weapon' ),
        ('summon', 'Summon'),
        ('extra', 'Extra' ),
    )

    catagory = models.CharField(
        max_length=20,
        choices=GB_CATAGORY_CHOICE,
        default='Extra'
    )

    GB_GENDER_CHOICE = (
        ('gran', 'Gran'),
        ('deeja', 'Deeja'),
        ('none', 'None')
    )

    gb_gender = models.CharField(
        max_length=20,
        choices=GB_GENDER_CHOICE,
        default='None'
    )

    path =  models.CharField(
        max_length=1000,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        catagoryandname = f'{self.catagory}-{self.name}'
        return catagoryandname
