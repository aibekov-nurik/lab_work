from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem
class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = Product.objects.filter(stock__gt=0).order_by('category__name', 'name')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('products_view')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('products_view')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('products_view')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('products_view')
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    quantity = int(request.POST.get('quantity', 1))

    if product.stock < quantity:
        return redirect('products_view')

    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        if cart_item.quantity + quantity > product.stock:
            cart_item.quantity = product.stock
        else:
            cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()
    return redirect('products_view')

def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart_item.delete()
    return redirect('cart_view')

def decrease_quantity_in_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_view')

def cart_view(request):
    cart_items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in cart_items)

    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


