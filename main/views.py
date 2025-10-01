from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm #CarForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    product_list = Product.objects.all()

    category = request.GET.get('category')
    if category:
        product_list = product_list.filter(category=category)

    filter_self = request.GET.get('my')
    if filter_self == 'true' and request.user.is_authenticated:
        product_list = Product.objects.filter(user=request.user)

    categories = Product.objects.values_list('category', flat=True).distinct()

    context = {
        'store' :   'Kickoff Standoff',
        'npm'   :   '2306275941',
        'name'  :   'Ahmad Aqeel Saniy',
        'class' :   'PBP A',
        'product_list' : product_list,
        'last_login' : request.COOKIES.get('last_login', 'Never'),
        'username' : request.user.username,
        'categories' : categories,
    }
    return render(request, 'main.html', context)

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form' : form}
    return render(request, 'add_product.html', context)

@login_required(login_url='/login')
def view_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product' : product
    }

    return render(request, 'product_detail.html', context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type='application/xml')

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize('json', product_list)
    return HttpResponse(json_data, content_type='application/json')

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize('xml', product_item)
        return HttpResponse(xml_data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse('Not Found', status=404)

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize('json', [product_item])
        return HttpResponse(json_data, content_type='application/json')
    except Product.DoesNotExist:
        return HttpResponse('Not Found', status=404)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully !')
            return redirect('main:login')
    context = {'form' : form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form' : form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')

def search_product(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )

    context = {
        'query' : query,
        'results' : results,
    }
    return render(request, 'search.html', context)

'''
def add_car(request):
    form = CarForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        carObj = Car 
        return redirect('main:show_main')

    context = {'form' : form}
    return render(request, 'add_car.html', context)
'''