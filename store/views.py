import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from PaycomUz.methods_subscribe_api import Subcribe

from .models import *
import json
import datetime
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz
from .utils import cookieCart, cartData
from clickuz import ClickUz
from django.views.decorators.csrf import csrf_exempt
from PaycomUz.status import ORDER_FOUND, ORDER_NOT_FOND, INVALID_AMOUNT
# Create your views here.
from .models import Product


class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        return self.ORDER_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        print(order_id)


class TestView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment


class Paycom:
    def __init__(self, order_id=None, order_type=None, amount=None):
         self.order_id = None
         self.order_type = None
         self.amount = None

    def check_order(self):
        # if self.order == True: #ma'lumotlari omborida huddi shunday buyurtma bor narxi ham to'g'ri keladi
        #     return ORDER_FOUND
        # else: #agar bunday buyurtma bo'lmasa
        #     return ORDER_NOT_FOND #yoki INVALID_AMOUNT #narxi to'g'ri kelmadi
        print(self.order_id)
        print(self.order_type)
        print(self.amount)
        return ORDER_FOUND

class Payment(APIView):
    def get(self, request):
        token = "61c05c25e2cfbecc12c7aa37_xWV0PE1peWbsRYb9RqicneD48AjY25M9uVQwq6Wg4rAuP1TcugCC94cnHuMCvFWQBfKKEAsAjJZA4ojfohEPppJYYmx0DROsJAMtPGsn56xrc3NToTyQd7zd0wx2vhs7XVm2wJadp3Pjqt0iUpgN861yJ6qehCx8C2MP8ZyQ1EohPhiYBtK8R7oXRIaUOAaoksnf9vzaZXt1hpMPza9rJZq2zme1BgH2w7mqtco3RrOFNGAGKKpPaeugXbsvXhsP6ykUY3Gcu2nbabc7dOQu2pviAa8qvGUgKhgMv9y8iZtWedrpWBmXc2JwYOv1UvdMtNUyM2f7gy4xyXyMBPSHCKkU5vBMTx7hJ6vjgITd2uAI5wT1IkpvneDVbNP2vBYNGamRiy"
        data = Subcribe(order_id=1, amount=5000.00, token=token).receipts_create()
        print(data)
        # except ObjectDoesNotExist:
        #     data = {}
        return Response(data)



def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems}

    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    order = data['order']
    items = data['items']
    cartItems = data['cartItems']

    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    order = data['order']
    items = data['items']
    cartItems = data['cartItems']
    url = ClickUz.generate_url(order_id='172', amount='150', return_url='http://example.com')
    print(url)
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, 'store/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_items, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        order_items.quantity += 1
    elif action == "remove":
        order_items.quantity -= 1

    order_items.save()

    if order_items.quantity <= 0:
        order_items.delete()

    return JsonResponse('Item was added', safe=False)




def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])

        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        url = "https://kassa-aparat-default-rtdb.firebaseio.com/orders.json"
        payload = json.dumps({
            # 'order': order,
            'id': order.id,
            'order_day': order.date_ordered,
            'city': order.city,
            'transaction_id': order.transaction_id,
            "number": order.get_cart_items()

        })
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "d40f61e7-bac1-e66b-0415-1169251aa220"
        }
        response = requests.request("POST", url, data=payload, headers=headers)

        from clickuz import ClickUz

        url = ClickUz.generate_url(order_id=f'{order.id}', amount=f'{order.get_cart_total}', return_url='success_payment')

        return redirect(url)

    else:
        print("user is not logged in")
    return JsonResponse("Payment completed", safe=False)



def success_payment(request, status, payment_id):
    print(status, payment_id)
    return render(request, "store/success_payment.html")