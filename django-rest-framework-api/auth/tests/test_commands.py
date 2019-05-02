# Django
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.six import StringIO


class CreateSuperuserTest(TestCase):

    def test_create_superuser(self):
        """
        Test that we can create a superuser by username
        """
        out = StringIO()

        call_command('createsu', 'mabrown', 'mabrown@example.com', stdout=out)

        self.assertIn('User \'mabrown\' created with default password', out.getvalue())
        user = get_user_model().objects.get(username='mabrown')
        self.assertTrue(user.check_password('django'))

    def test_create_superuser_handles_duplicates(self):
        """
        Test that we can create a superuser by username
        """
        out = StringIO()
        get_user_model().objects.create_superuser(username='mabrown', email='mabrown@example.com', password='django')

        call_command('createsu', 'mabrown', 'mabrown@example.com', stdout=out)

        self.assertIn('User \'mabrown\' already exists', out.getvalue())