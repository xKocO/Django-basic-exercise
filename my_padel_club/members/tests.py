from django.test import TestCase
from .models import Member
from datetime import date


class ProperMemberTest(TestCase):
    def test_setUpMember(self):
        testmember = Member.objects.create(
            firstname="John",
            lastname="testing",
            phone=3516885544,
            Joined_date="2001-05-11",
        )

        print(
            f"Name: {testmember.firstname}, "
            f"Lastname: {testmember.lastname}, "
            f"Phone: {testmember.phone}, "
            f"Joined date: {testmember.Joined_date}"
        )

        self.assertEqual(str(testmember), "John testing")
