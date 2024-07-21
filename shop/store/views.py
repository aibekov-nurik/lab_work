from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import CategoryForm, ProductForm, ProductSearchForm


def products_view(request):
    form = ProductSearchForm(request.GET)
    products = Product.objects.filter(stock__gt=0).order_by('category', 'name')
    if form.is_valid() and form.cleaned_data['query']:
        products = products.filter(name__icontains=form.cleaned_data['query'])
    return render(request, 'products.html', {'products': products, 'form': form})



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

def product_edit_view(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_view', id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_edit.html', {'form': form, 'product': product})

def product_delete_view(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('products_view')
    return render(request, 'product_confirm_delete.html', {'product': product})


