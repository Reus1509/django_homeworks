from django.core.management.base import BaseCommand
from hw_2.models import Order, Client, Product


class Command(BaseCommand):
    help = "Print name, email, phone_number and address"

    def handle(self, *args, **options):
        user = Client(client=options.get(pk=pk),
                      products='JhonSmith@gmail.com',
                      order_sum='+79785222222')

        user.save()
        self.stdout.write(f'{user}')