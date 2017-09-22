from django.shortcuts import render
from django.views.generic import TemplateView

from ..models import Member

from ..forms import InactiveMemberForm

class InactiveMemberView(TemplateView):
    template = 'inactive_member.html'

    def get(self, request):
        form = InactiveMemberForm()

        return render(
            request,
            self.template,
            {
                'form': form
            }
        )

    # def post(self, request):
    #     form = InactiveMemberForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    #     return render(
    #         request,
    #         self.template,
    #         {
    #             'form': form
    #         }
    #     )
