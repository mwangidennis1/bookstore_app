from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    def test_case_user(self):
        User = get_user_model()
        user =User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username,'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user=User.objects.create_superuser(
            username='ali',
            email='ali@email.com',
            password='testpass124'
        )
        self.assertEqual(admin_user.username, 'ali')
        self.assertEqual(admin_user.username,'ali@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(admin_user.is_superuser)