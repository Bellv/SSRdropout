from django.test import TestCase

from ..models import Member


class MemberTest(TestCase):
    def setUp(self):
        self.member = Member()

    def test_save_member(self):
        self.member = Member()

        self.member.name = 'Belly'
        self.member.gb_id = '12345678'
        self.member.gb_name = 'マスター'
        self.member.save()

        self.assertTrue(self.member.id)
