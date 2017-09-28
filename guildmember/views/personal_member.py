from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Member


class PersonalMemberView(TemplateView):
    template = 'personal_member.html'

    def get(self, request):
        members = Member.objects.all().filter(status='active')

        return render(
            request,
            self.template,
            {
                'members': members
            }
        )
