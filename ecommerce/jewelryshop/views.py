# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings


# def index(request):
#     if request.method == 'POST':
#         message = request.POST['message']
#         send_mail('Contact Form', 
#                   message,
#                   settings.EMAIL_HOST_USER,
#                   'elmurodazodov777@gmail.com',
#                   fail_silently=False)
#     return render(request, 'index.html')

import django
from django.contrib.auth.models import User
from store.models import Address, Cart, Category, Order, Product
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views import View
import decimal
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # for Class Based Views
from .forms import *

# Create your views here.

# ==================================================
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from jewelryshop.usecases import testpermission


# from first_project.usecases import testpermission

from store.forms import ProductForm
from store.models import Product


# 1
class ProductListView(ListView):
    modal = Product
    template_name = 'products.html'

    def get_queryset(self):
        return Product.objects.all()

# 2
class AddProductView(CreateView):
    modal = Product
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = '/product/'

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            product = form.save(commit=False)
            product.author = self.request.user
            product.save()
        return redirect('products_view')
# 3 
class ProductDetailsView(DetailView):
    modal = Product
    template_name = 'product_details.html'

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])
    

@login_required
@user_passes_test(testpermission, login_url='products_view')
def delete_product(request, product_id: int):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('products_view')
