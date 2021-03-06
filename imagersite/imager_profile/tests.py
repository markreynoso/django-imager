"""Tests for imagersite models."""
from django.test import TestCase

import factory

from imager_profile.models import ImagerProfile, User


class UserFactory(factory.django.DjangoModelFactory):
    """Class that inherits from factory."""

    class Meta:
        """Default user for all new instances of User."""

        model = User
    username = 'Bob'
    email = 'bob@example.com'


class ProfileTest(TestCase):
    """Test class for ImagerProfile model."""

    def setUp(self):
        """Setup user for testing."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.save()
        self.user.profile.phone = '206-555-5555'
        self.user.profile.website = 'www.website.com'
        self.user.profile.location = 'Seattle, WA'
        self.user.profile.fee = 100.00
        self.user.profile.camera = 'CANON'
        self.user.profile.services = 'OTHER'
        self.user.profile.photo_styles = 'COLOR'
        self.user.profile.save()

    def test_one_user(self):
        """Test user profile is created."""
        one_user = User.objects.get()
        self.assertIsNotNone(one_user.profile)

    def test_profile_website(self):
        """"Test profile website it www.website.com."""
        user = User.objects.get()
        self.assertEqual(user.profile.website, 'www.website.com')

    def test_user_phone_is_correct(self):
        """Test phone is 206-555-5555."""
        user = User.objects.get()
        self.assertEqual(user.profile.phone, '206-555-5555')

    def test_user_location_is_seattle_wa(self):
        """Test user phonne location is seattle."""
        user = User.objects.get()
        self.assertEqual(user.profile.location, 'Seattle, WA')

    def test_user_fee_correct(self):
        """Test user fee is 100.00."""
        user = User.objects.get()
        self.assertEqual(user.profile.fee, 100.00)

    def test_user_camera_is_canon(self):
        """Test user camera defaults to canon."""
        user = User.objects.get()
        self.assertEqual(user.profile.camera, ['CANON'])

    def test_user_services_is_other(self):
        """Test user services defaults to other."""
        user = User.objects.get()
        self.assertEqual(user.profile.services, ['OTHER'])

    def test_user_photo_styles_is_color(self):
        """Test user photo styles defaults to color."""
        user = User.objects.get()
        self.assertEqual(user.profile.photo_styles, ['COLOR'])

    def test_user_is_active_true(self):
        """Test user is active by default."""
        user = User.objects.get()
        self.assertTrue(user.profile.is_active)
