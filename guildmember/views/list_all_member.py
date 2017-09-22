from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Member


class MemberListView(TemplateView):
    template = 'list_all_member.html'

    def get(self, request):
        members = Member.objects.all().filter(status='active')

        return render(
            request,
            self.template,
            {
                'members': members
            }
        )
