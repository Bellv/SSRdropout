from django.contrib import admin

from .models import Member, WeaponSummon, Pool, Status, Friend, Job


admin.site.register(Member)
admin.site.register(WeaponSummon)
admin.site.register(Pool)
admin.site.register(Status)
admin.site.register(Friend)
admin.site.register(Job)
