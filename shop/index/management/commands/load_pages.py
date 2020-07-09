from django.core.management.base import BaseCommand, CommandError
from index.models import Page
import json

class Command(BaseCommand):
  
    def handle(self, *args, **options):
        print('Start command')
        Page.objects.all().delete()

        with open('pages.json') as f:
            data = json.load(f)

        for line in data:
            p = Page()
            p.title = line['title']
            p.content = line['content']
            p.save()