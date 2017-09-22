from django.conf.urls import url

from .views.list_all_member import MemberListView
from .views.add_member import MemberAddView
from .views.inactive_member import InactiveMemberView

urlpatterns = [
    url(
        r'^$',
        MemberListView.as_view(),
        name='list_all_member'
    ),

    url(
        r'^addmember/$',
        MemberAddView.as_view(),
        name='add_member'
    ),

    url(
        r'^inactivemember/$',
        InactiveMemberView.as_view(),
        name='inactive_member'
    )
]
