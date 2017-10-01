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


class Job(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    GB_GENDER_CHOICE = (
        ('gran', 'Gran'),
        ('deeja', 'Deeja'),
    )
    gb_gender = models.CharField(
        max_length=20,
        choices=GB_GENDER_CHOICE
    )
    image_path =  models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name


class Friend(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    image_path =  models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name


class Power(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )
    job = models.ForeignKey(Job)
    ELEMENT_CHOICE = (
        ('none', 'None Element'),
        ('light', 'Light'),
        ('dark', 'Dark'),
        ('wind', 'Wind'),
        ('fire', 'Fire'),
        ('water', 'Water'),
        ('earth', 'Earth'),
    )
    element = models.CharField(
        max_length=20,
        choices=ELEMENT_CHOICE,
        default='none'
    )
    estimate_dmg = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    weak_dmg = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'{self.member.name} - {self.element}'


class Weaponsummon(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    TYPE_WEAPON_OR_SUMMON_CHOICE = (
        ('weapon', 'Weapon'),
        ('summon', 'Summon'),
    )
    type_wep_sum = models.CharField(
        max_length=20,
        choices=TYPE_WEAPON_OR_SUMMON_CHOICE,
        default='weapon'
    )
    ELEMENT_CHOICE = (
        ('none', 'None Element'),
        ('light', 'Light'),
        ('dark', 'Dark'),
        ('wind', 'Wind'),
        ('fire', 'Fire'),
        ('water', 'Water'),
        ('earth', 'Earth'),
    )
    element = models.CharField(
        max_length=20,
        choices=ELEMENT_CHOICE,
        default='none'
    )
    image_path = image_path =  models.CharField(
        max_length=300,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name


class Pool(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE
    )
    weaponsummon = models.ForeignKey(
        Weaponsummon,
        on_delete=models.CASCADE
    )
    TYPE_WEAPON_OR_SUMMON_CHOICE = (
        ('weapon', 'Weapon'),
        ('summon', 'Summon'),
    )
    type_wep_sum = models.CharField(
        max_length=20,
        choices=TYPE_WEAPON_OR_SUMMON_CHOICE,
        default='weapon'
    )
    ORDER_CHOICE = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
        ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
    )
    order =  models.CharField(
        max_length=1,
        choices=ORDER_CHOICE,
        default='0'
    )
    STAR_CHOICE = (
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),
    )
    star =  models.CharField(
        max_length=1,
        choices=STAR_CHOICE,
        default='0'
    )

    def __str__(self):
        return f'{self.member.name} - {self.weaponsummon.name} - {self.order}'
