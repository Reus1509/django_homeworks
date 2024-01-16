from django.core.management.base import BaseCommand
from hw_2.models import Client


class Command(BaseCommand):
    help = "Print name, email, phone_number and address"

    def handle(self, *args, **options):
        user = Client(name='Jhon',
                      email='JhonSmith@gmail.com',
                      phone_number='+79785222222',
                      address='New York, 6-th ave, 231')
        user.save()
        self.stdout.write(f'{user}')
