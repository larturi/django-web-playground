from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@correo.com', password='test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEquals(exists, True)
