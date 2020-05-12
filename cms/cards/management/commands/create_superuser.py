from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a test super user with the given password'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        username = options.get('username')
        password = options.get('password')
        try:
            User = get_user_model()
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username,
                                              'admin@example.com',
                                              password)
                print('Superuser %s with password %s successfully created!\n'
                      % (username, password))
            else:
                print('Superuser %s with password %s already exists!\n'
                      % (username, password))
        except Exception as e:
            print('ERROR: Can\'t create superuser.\n%s\n' % e)
