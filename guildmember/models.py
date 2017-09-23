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

    GB_CHARACTER_CHOICE = (
        ('deeja', 'Deeja'),
        ('gran', 'Gran' ),
    )

    gb_character = models.CharField(
        max_length=20,
        choices=GB_CHARACTER_CHOICE,
        default='deeja'
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
