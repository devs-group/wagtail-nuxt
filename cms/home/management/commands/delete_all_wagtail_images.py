import os

from django.core.management.base import BaseCommand
from wagtail.images.models import Image


class Command(BaseCommand):
    help = 'For local development delete all linked wagtail images to prevent key: message error. You will be prompted.'

    def yes_or_no(self, question):
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
        else:
            return self.yes_or_no("Invalid input: %s" % (question))

    def handle(self, *args, **options):
        if os.environ.get('ENVIRONMENT') is 'production':
            print("Command not allowed in production!")
            return

        images = Image.objects.all()
        if not images:
            print("No wagtail images found to delete.")
            return

        if self.yes_or_no('Are you sure you want to delete %d wagtail images?' % (len(images))):
            try:
                Image.objects.all().delete()
            except Exception as e:
                print('ERROR: Can\'t delete wagtail images.\n%s\n' % e)
