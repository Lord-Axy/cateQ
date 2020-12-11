from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect


# Create your views here.
def home(request):
    famous_products = Product.objects.filter(is_famous_product=True).order_by('?')
    categories = Categories.objects.all().order_by('?')
    return render(request,"home.html",{'famous_products':famous_products,'categories':categories})

def categories(request):
    page = request.GET.get('page',1)
    categories = Categories.objects.all()
    pages = Paginator(categories, 9)
    categories = pages.page(page)
    famous_products = Product.objects.filter(is_famous_product=True).order_by('?')
    return render(request,"shop.html",{"categories":categories.object_list,"current_page":page,"page_range":categories,"num_pages":pages.page_range,'famous_products':famous_products})

def products(request):
    category = request.GET.get('category')
    page = request.GET.get('page',1)
    category = Categories.objects.get(pk=category)
    products = Product.objects.filter(category=category)
    pages = Paginator(products, 9)
    products = pages.page(page)
    famous_products = Product.objects.filter(is_famous_product=True).order_by('?')
    return render(request,"products.html",{"products":products.object_list,"current_page":page,"page_range":products,"num_pages":pages.page_range,'category':category,'famous_products':famous_products})

def product_detail(request):
    id = request.GET.get("prod_id")
    product = Product.objects.get(id=id)
    features = product.features.strip()
    features = features.replace('\r\n','')
    features = features.split('~')
    famous_products = Product.objects.filter(is_famous_product=True).order_by('?')
    return render(request,"product_detail.html",{"product":product,"features":features[1:],'famous_products':famous_products})

def faq(request):
    famous_products = Product.objects.filter(is_famous_product=True).order_by('?').order_by('?')
    return render(request,"faq.html",{'famous_products':famous_products})

def about(request):
    famous_products = Product.objects.filter(is_famous_product=True).order_by('?')
    return render(request,"about.html",{'famous_products':famous_products})
    
def send_mail(request):
    name = request.GET.get("name")
    phone = request.GET.get("number")
    email = request.GET.get("email")
    subject = request.GET.get("subject")
    content = request.GET.get("content")
    from django.core.mail import send_mail
    from django.http import HttpResponse
    try:
        send_mail(subject, content + "\n\nPhone number:"+phone+"\n\n Email:"+email,
        'contact@cateq.org',
        ['cateqexports@gmail.com'],
        fail_silently=False,
        )
        #return HttpResponse(status=200)
        return HttpResponse('Invalid header found.')
    except Exception as e:
        #return HttpResponse(status=400)
        return HttpResponse(name+":0"+phone+":0"+email+":0"+subject+":0"+content+":0")
    
def about_us(request):
    famous_products = Product.objects.filter(is_famous_product=True).order_by('?')
    return render(request,"contact.html",{'famous_products':famous_products})

def view_404(request):
    print('here')
    response = redirect('/')
    return response