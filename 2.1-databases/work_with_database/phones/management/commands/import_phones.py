import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
import re

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phone = Phone(name=phone["name"], price=phone["price"], image=phone["image"], release_date=phone["release_date"], lte_exists=phone["lte_exists"], slug=slugify(phone["name"]))
            phone.save()
            
