from hw_2.models import Client, Order
from datetime import datetime, timedelta
from django.shortcuts import render


def client_orders(request, id_client: int):
    products = {}

    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(buyer=client).all()

    for order in orders:
        products[order.id] = str(order.products.all()).replace('<QuerySet [<', '').replace('>]>', '').split('>, <')

    return render(request, 'hw_3/client_orders.html', {'client': client, 'orders': orders, 'products': products})


def client_products_sorted(request, id_client: int, days: int):
    products = []
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days)
    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(buyer=client, date_create_order__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'shop_app/client_all_products_from_orders.html',
                  {'client': client, 'product_set': product_set, 'days': days})
