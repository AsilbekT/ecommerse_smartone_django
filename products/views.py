from django.shortcuts import render
from .models import Product
# Create your views here.


def products(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products.html", context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {"product_details": product}
    return render(request, "products.html", context)