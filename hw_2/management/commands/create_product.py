from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = "Print name, description, price and count"

    def handle(self, *args, **options):
        product = Product(name='TV',
                      description='Плазменный телевизор с очень хорошей качественной картинкой',
                      price=39999.99,
                      count='5')
        product.save()
        self.stdout.write(f'{product}')
