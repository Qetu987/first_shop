from django.core.management.base import BaseCommand, CommandError
from index.models import Page
import json

class Command(BaseCommand):
  
    def handle(self, *args, **options):
        print('Start command')
        Page.objects.all().delete()

        with open('pages.json') as f:
            templates = json.load(f)

        for line in templates:
            title = line['title']
            content = line['content']

            p = Page()
            p.title = title
            p.content = content
            p.save()