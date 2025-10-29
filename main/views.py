from itertools import product

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
import json


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    product_list = Product.objects.all()

    search_query = request.GET.get('search')
    if search_query:
        product_list = product_list.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query) |
            Q(brand__icontains=search_query) |
            Q(user__username__icontains=search_query)
        )

    filter_category = request.GET.get('category')
    if filter_category and filter_category != 'all':
        product_list = product_list.filter(category=filter_category)

    filter_self = request.GET.get('filter')
    if filter_self == 'my' and request.user.is_authenticated:
        product_list = product_list.filter(user=request.user)

    raw_category = Product.objects.values_list('category', flat=True)
    categories = sorted(set(raw_category))

    context = {
        'store': 'Kickoff Standoff',
        'npm': '2306275941',
        'name': 'Ahmad Aqeel Saniy',
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username,
        'filter_category': filter_category,
        'search': search_query or '',
    }
    return render(request, 'main.html', context)


@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, 'Product Added Successfully !')
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, 'add_product.html', context)


@login_required(login_url='/login')
def view_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, 'product_detail.html', context)


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type='application/xml')


def show_json(request):
    product_list = Product.objects.all()
    product_data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'rating': product.rating,
            'is_stock_available': product.is_stock_available,
            'user_id': product.user_id
        }
        for product in product_list
    ]
    return JsonResponse(product_data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize('xml', product_item)
        return HttpResponse(xml_data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse('Not Found', status=404)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        product_data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'rating': product.rating,
            'is_stock_available': product.is_stock_available,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(product_data)
    except Product.DoesNotExist:
        return HttpResponse({'detail': 'Not found'}, status=404)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['toast'] = {
                'type': 'success',
                'title': 'Welcome!',
                'message': 'Account created successfully! Please login.'
            }
            return redirect('main:login')
        else:
            request.session['toast'] = {
                'type': 'error',
                'title': 'Registration Failed',
                'message': 'Registration failed. Please check your information.'
            }

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['toast'] = {
                'type': 'success',
                'title': 'Welcome Back!',
                'message': f'Hello {user.username}, you have been logged in successfully!'
            }
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            request.session['toast'] = {
                'type': 'error',
                'title': 'Login Failed',
                'message': 'Invalid username or password.'
            }
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    request.session['toast'] = {
        'type': 'info',
        'title': 'Goodbye!',
        'message': 'You have been logged out successfully.'
    }
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == 'POST':
        form.save()
        messages.success(request, f'Product "{product.name}" updated successfully!')
        return redirect('main:show_main')

    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product_name = product.name
    product.delete()
    messages.success(request, f'Product "{product_name}" deleted successfully!')
    return HttpResponseRedirect(reverse('main:show_main'))


@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    try:
        name = strip_tags(request.POST.get('name', '').strip())
        price = request.POST.get('price', '').strip()
        description = strip_tags(request.POST.get('description', '').strip())
        thumbnail = request.POST.get('thumbnail', '').strip()
        category = request.POST.get('category', '').strip()
        is_featured = request.POST.get('is_featured') == 'on'
        stock = request.POST.get('stock', '0').strip()
        brand = strip_tags(request.POST.get('brand', '').strip())

        # Validation
        if not name or not price or not category:
            return JsonResponse({
                'success': False,
                'error': 'Name, price, and category are required fields.'
            }, status=400)

        # Create product
        new_product = Product(
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            stock=stock,
            brand=brand,
            user=request.user
        )
        new_product.save()

        return JsonResponse({
            'success': True,
            'message': 'Product created successfully!',
            'product_name': new_product.name,
            'product_id': str(new_product.id)
        }, status=201)

    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    try:
        product = Product.objects.get(id=id, user=request.user)
        product_name = product.name
        product.delete()

        return JsonResponse({
            'success': True,
            'message': 'Product deleted successfully!',
            'product_name': product_name
        })

    except Product.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Product not found or you do not have permission to delete it.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@csrf_exempt
@require_POST
@login_required
def edit_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)

        # Get the data from the request
        name = strip_tags(request.POST.get('name', '').strip())
        price = request.POST.get('price', '').strip()
        description = strip_tags(request.POST.get('description', '').strip())
        thumbnail = request.POST.get('thumbnail', '').strip()
        category = request.POST.get('category', '').strip()
        is_featured = request.POST.get('is_featured') == 'on'
        stock = request.POST.get('stock', '0').strip()
        brand = strip_tags(request.POST.get('brand', '').strip())

        # Validation
        if not name or not price or not category:
            return JsonResponse({
                'success': False,
                'error': 'Name, price, and category are required fields.'
            }, status=400)

        # Update the product
        product.name = name
        product.price = price
        product.description = description
        product.thumbnail = thumbnail
        product.category = category
        product.is_featured = is_featured
        product.stock = stock
        product.brand = brand
        product.save()

        return JsonResponse({
            'success': True,
            'message': 'Product updated successfully!',
            'product_name': product.name,
            'product_id': str(product.id)
        })

    except Product.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Product not found or you do not have permission to edit it.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


@require_POST
def clear_toast(request):
    if 'toast' in request.session:
        del request.session['toast']
    return JsonResponse({'success': True})