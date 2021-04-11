import random 
from django.shortcuts import render

from apps.product.models import Product

def frontpage(request):
    products=list(Product.objects.all())
    newest_products=random.sample(products, 12)
    return render(request,"core/frontpage.html",{'newest_products' : newest_products})

def about(request):
    return render(request,"core/about.html")