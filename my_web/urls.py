
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('categories/', views.categories, name='categories'),
    path('add-products/', views.add_products, name='add_products'),
    path('add-order/<int:table_id>/', views.add_order, name='add_order'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('tables/', views.table, name='tables'),
]
