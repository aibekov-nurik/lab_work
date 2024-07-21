from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import CategoryForm, ProductForm

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_view(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'product.html', {'product': product})

def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_view')
    else:
        form = CategoryForm()
    return render(request, 'category_add.html', {'form': form})

def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_view', id=product.id)
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})
