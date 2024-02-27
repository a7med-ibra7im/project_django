from django.urls import path
from . import views 
from django.views.i18n import set_language



app_name ='products'


urlpatterns = [
    path('', views.product_list),
    path('<slug:slug>', views.product_detail , name='product_detail'),
    path('add_product/',views.add_product, name='add_product'),
    path('i18n/', set_language, name='set_language'),

] 