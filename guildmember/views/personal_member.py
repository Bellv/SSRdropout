from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Member, Job, Friend, Weaponsummon, Power


class PersonalMemberView(TemplateView):
    template = 'personal_member.html'

    def retrive_member_data(self, member_id):
        member = Member.objects.get(id=member_id)

        try:
            character = Job.objects.get(
                name=member.gb_class,
                gb_gender=member.gb_gender
            )

        except:
            character = None

        return member

    def retrive_waifu_data(self, member_id):
        member = Member.objects.get(id=member_id)

        try:
            waifu = Friend.objects.get(name=member.gb_waifu)
        except:
            waifu = None

        return waifu

    def retrive_power_data(self, member_id):
        member = Member.objects.get(id=member_id)

        try:
            power = Power.objects.get(member=member)
        except:
            power = None

        return power

    def get(self, request, **kwargs):
        member = Member.objects.all()

        member = self.retrive_member_data(
            self.kwargs['member_id']
        )

        waifu = self.retrive_waifu_data(
            self.kwargs['member_id']
        )
       
        power = self.retrive_power_data(
            self.kwargs['member_id']
        )

        weapon = Weaponsummon.objects.get(name="Sakura Wand")
        weapon2 = Weaponsummon.objects.get(name="Sakura Wand")
        weapon3 = Weaponsummon.objects.get(name="Sakura Wand")
        summon = Weaponsummon.objects.get(name="Sakura Wand")

        return render(
            request,
            self.template,
            {
                'member': member,
                'waifu': waifu,
                'power': power,
                'weapon': weapon,
                'weapon2': weapon2,
                'weapon3': weapon3,
                'summon': summon

            }
        )
