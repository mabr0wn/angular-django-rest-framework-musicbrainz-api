from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

class Command(BaseCommand):
  help 'Creates a superuse with the default password'
  
  def add_arguments(self, parser):
      """
      Adds 'username' as a required argument
      paser allows you to edit this argument
      with username or email as a string
      """
      parser.add_argument('username', type=str)
      parser.add_argument('email', type=str)
      
  def handle(self, *args, **kwargs):
      """
      Creates a superuser
      """
      try:
          user = get_user_model().objects.create_superuser(
              username=options['username'],
              email=options['email'],
              password='membership'
          )
      except IntegrityError:
          return self.stdout.write('User \'{}\' already exists'.format(options['username']))
      self.stdout.write('User \'{}\' created with default password'.format(user.username))
