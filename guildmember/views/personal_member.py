from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Member, Job, Friend, Weaponsummon


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

        # try:
        #     waifu = Friend.objects.get(name=member.gb_waifu)
        # except:
        #     waifu = None

        return member, character

    def get(self, request, **kwargs):
        member, character = self.retrive_member_data(
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
                'character': character,
                'weapon': weapon,
                'weapon2': weapon2,
                'weapon3': weapon3,
                'summon': summon

            }
        )
