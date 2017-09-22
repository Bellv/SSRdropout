from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from ..forms import AddMemberForm


class MemberAddView(TemplateView):
    template = 'add_member.html'

    def get(self, request):
        form = AddMemberForm()

        return render(
            request,
            self.template,
            {
                'form': form
            }
        )

    def post(self, request):
        form = AddMemberForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse(
                'list_all_member',
                )
            )

        return render(
            request,
            self.template,
            {
                'form': form
            }
        )
