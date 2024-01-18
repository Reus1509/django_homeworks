from django.core.management.base import BaseCommand
from hw_2.models import Product


class Command(BaseCommand):
    help = "create product"

    def add_arguments(self, parser):

        parser.add_argument('name', type=str, help='name of products')
        parser.add_argument("description", type=str, help="product description")
        parser.add_argument("cost", type=float, help="price of product")
        parser.add_argument("quantity", type=int, help="quantity of product")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('cost')
        count = kwargs.get('quantity')

        product = Product(name=name, description=description, price=price,  count=count)
        product.save()

        self.stdout.write(f'{product}')
