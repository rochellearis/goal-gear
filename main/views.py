import datetime
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    # Ambil semua produk
    products = Product.objects.all()

    # Filter kategori
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    # Filter "my"
    filter_type = request.GET.get('filter')
    if filter_type == "my":
        products = products.filter(user=request.user)

    # Search
    q = request.GET.get('q', '')
    if q:
        products = products.filter(
            Q(name__icontains=q) |
            Q(category__icontains=q) |
            Q(description__icontains=q)
        )

    # Deteksi apakah ini HOME (tanpa filter, kategori, atau search)
    is_home = not filter_type and not category and not q

    if is_home:
        featured_products = products.filter(is_featured=True)
        non_featured_products = products.exclude(is_featured=True)
    else:
        featured_products = None
        non_featured_products = products  # tampil semua (campur featured)

    context = {
        'app_name': 'Goal Gear',
        'featured_products': featured_products,
        'product_list': non_featured_products,
        'category': category,
        'q': q,
        'last_login': request.user.last_login or 'Never'
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    filter_type = request.GET.get('filter', 'all')
    category = request.GET.get('category')
    query = request.GET.get('q', '').strip()

    products = Product.objects.all()

    # Filter berdasarkan kategori (jika ada)
    if category:
        products = products.filter(category__iexact=category)

    # Filter produk milik user sendiri
    if filter_type == 'my' and request.user.is_authenticated:
        products = products.filter(user=request.user)

    # Filter berdasarkan pencarian
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )

    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand or None,
            'rating': product.rating,
            'user_id': product.user.username if product.user else None,
            'user_username': product.user.username if product.user else None,
            'is_owner': request.user.is_authenticated and product.user == request.user,
            'detail_url': reverse('main:show_product', args=[product.id]),
            'delete_url': reverse('main:delete_product', args=[product.id]),
        }
        for product in products
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        try:
            thumbnail = product.thumbnail.url if getattr(product, 'thumbnail', None) else product.thumbnail
        except Exception:
            thumbnail = product.thumbnail or ''

        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': thumbnail,
            'price': float(product.price) if product.price is not None else None,
            'stock': int(getattr(product, 'stock', 0)),
            'brand': product.brand or None,
            'rating': float(product.rating) if getattr(product, 'rating', None) is not None else None,
            'created_at': product.created_at.isoformat() if getattr(product, 'created_at', None) else None,
            'is_featured': bool(getattr(product, 'is_featured', False)),
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # AJAX response
                return JsonResponse({
                    'success': True,
                    'redirect_url': reverse('main:login')
                })
            else:
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = {field: [str(e) for e in errs] for field, errs in form.errors.items()}
                return JsonResponse({
                    'success': False,
                    'error': errors
                })
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'redirect_url': reverse('main:show_main')
                })
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = {field: [str(e) for e in errs] for field, errs in form.errors.items()}
                return JsonResponse({
                    'success': False,
                    'error': errors
                })
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    # Cookie sementara untuk menandai logout
    response.set_cookie('logged_out', 'true', max_age=3)  # hilang setelah 3 detik
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    thumbnail = request.POST.get("thumbnail")
    category = request.POST.get("category")
    is_featured = request.POST.get("is_featured") == 'on'  # untuk checkbox
    stock = request.POST.get("stock")
    brand = request.POST.get("brand")

    # pastikan ada user yang login
    user = request.user if request.user.is_authenticated else None

    # buat instance product baru
    new_product = Product(
        user=user,
        name=name,
        price=price or 0,
        description=description or "No description",
        thumbnail=thumbnail or None,
        category=category,
        is_featured=is_featured,
        stock=stock or 0,
        brand=brand or "None",
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)