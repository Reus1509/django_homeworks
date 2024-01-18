from django.core.management.base import BaseCommand
from hw_2.models import Client, Order, Product


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("id_client", type=int, help="client ID")
        parser.add_argument('-p', '--id_product', nargs='+', help="client ID", required=True)

    def handle(self, *args, **kwargs):
        client = kwargs.get('id_client')
        products: list = kwargs.get('id_product')                         #запись в id_product  параметров из командной строки

        client = Client.objects.filter(pk=client).first()

        order = Order(client=client)
        total_price = 0
        for i in range(0, len(products)):
            product = Product.objects.filter(pk=products[i]).first()
            total_price += float(product.price)
            order.order_sum = total_price
            order.save()
            order.products.add(product)