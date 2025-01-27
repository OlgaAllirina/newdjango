import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone = Phone(
                name=phone['name'],
                image=phone['image'],
                price=int(phone['price']),
                release_data=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=phone['name'].lower().replace(' ', '_')
            )
            phone.save()


