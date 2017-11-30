from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Member, Job, Friend, Weaponsummon, Power


class PersonalMemberView(TemplateView):
    template = 'personal_member.html'

    def retrive_job_image(self, member):
        try:
            job = Job.objects.get(
                name=member.gb_class,
                gb_gender=member.gb_gender
            )

        except:
            job = None

        return job

    def retrive_waifu_data(self, member):
        try:
            waifu = Friend.objects.get(name=member.gb_waifu)
        except:
            waifu = None

        return waifu

    def retrive_power_data(self, member):
        try:
            power = Power.objects.get(member=member)
        except:
            power = None

        return power

    # def retrive_weapon_light(self, member):
    #     weapon_light = []

    #     try:
    #         weapon_light_1 = Pool.objects.get(
    #             member = member,
    #             pool_element = 'light',
    #             order = 1
    #         )
    #         weapon_light.append(weapon_light_1)
    #     except:
    #         power = None

    #     return weapon_light

    def get(self, request, **kwargs):
        member = Member.objects.get(id=self.kwargs['member_id'])

        job = self.retrive_job_image(member)
        waifu = self.retrive_waifu_data(member)
        power = self.retrive_power_data(member)

        # weapon_light = self.retrive_weapon_light(member)
        # print (weapon_light)
        weapon = Weaponsummon.objects.get(name="Aschallon Lumen")
        weapon2 = Weaponsummon.objects.get(name="Luminiera Sword Omega")
        weapon3 = Weaponsummon.objects.get(name="Cosmic Sword BAL")
        summon = Weaponsummon.objects.get(name="Lucifer")

        return render(
            request,
            self.template,
            {
                'member': member,
                'job': job,
                'waifu': waifu,
                'power': power,
                'weapon': weapon,
                'weapon2': weapon2,
                'weapon3': weapon3,
                'summon': summon

            }
        )
