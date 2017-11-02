from django.conf.urls import url

from . import views
from .views.list_all_member import MemberListView
from .views.add_member import MemberAddView
from .views.inactive_member import InactiveMemberView
from .views.personal_member import PersonalMemberView
from .views import guildmember_api

urlpatterns = [
    url(r'^$',
        MemberListView.as_view(),
        name='list_all_member'
    ),
    url(r'^addmember/$',
        MemberAddView.as_view(),
        name='add_member'
    ),
    url(r'^inactivemember/$',
        InactiveMemberView.as_view(),
        name='inactive_member'
    ),
    url(r'^(?P<member_id>[0-9]+)/(?P<member_name>[A-Za-z_/,\.-]+)/$',
        PersonalMemberView.as_view(),
        name='personal_member'
    ),
    url(r'^memberlist$',
        guildmember_api.ListCreateMember.as_view(),
        name='member_list'
    ),
    url(r'(?P<pk>\d+)$',
        guildmember_api.RetrieveUpdateDestroyMember.as_view(),
        name='member_detail'
    ),
    url(r'^poollist$',
        guildmember_api.ListCreatePool.as_view(),
        name='pool_list'
    ),
]
