from django.shortcuts import render,get_object_or_404,redirect

from django.http import HttpResponse
from django.utils.translation import activate
from .models import Product
from django.core.paginator import Paginator
from .forms import ProductForm
from django.urls import reverse




def add_product(request):
    product_list = Product.objects.all()

    if request.method == 'POST':
        add_book = ProductForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect('product_list')

    context = {
        'form': ProductForm(),
    }
    return render(request, 'Product/add_product.html', context)


def product_list(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 3)  
    page_number = request.GET.get("page")
    product_list = paginator.get_page(page_number)
    
    context = {
    'product_list':product_list,
    'form' : ProductForm(),
    }
    
    return render(request,'Product/product_list.html' , context)



def product_detail(request , slug):

    product_detail = Product.objects.get(PRDSlug=slug)
    

    context = {'product_detail':product_detail}
    

    return render(request,'Product/product_detail.html' , context)



def my_view(request):
    # Determine user language preference or use site default
    user_language = request.LANGUAGE_CODE
    activate(user_language)
    # Your view logic here