from django.test import TestCase
from .models import UserAccount

# Create your tests here.

class ProfileTest(TestCase):

    def test_useraccount_model_has_profile(self):
        user = UserAccount(
            email="andrewnick@gmail.com",
            username="andynick",
            password="andy1234"
        )
        user.save()

        self.assertTrue(
            hasattr(user, 'profile')
        )
