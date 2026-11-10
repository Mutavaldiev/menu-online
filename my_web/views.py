
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Dish, Table, Order, OrderItem


def index(request):
    tables = Table.objects.all()
    return render(request, 'index.html', {'tables': tables})


def menu(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {
        'categories': categories,
        'dishes': dishes
    })


def categories(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST['name'])
        return redirect('categories')

    return render(request, 'categories.html', {
        'categories': Category.objects.all()
    })


def add_products(request):
    if request.method == 'POST':
        Dish.objects.create(
            name=request.POST['name'],
            category_id=request.POST['category'],
            price=request.POST['price']
        )
        return redirect('menu')

    return render(request, 'add_products.html', {
        'categories': Category.objects.all()
    })


def add_order(request, table_id):
    table = get_object_or_404(Table, id=table_id)

    if table.is_occupied:
        return redirect('index')

    if request.method == 'POST':
        order = Order.objects.create(
            table=table,
            customer_name=request.POST['customer_name']
        )

        for dish in Dish.objects.all():
            quantity = int(request.POST.get(f'dish_{dish.id}', 0))

            if quantity > 0:
                OrderItem.objects.create(
                    order=order,
                    dish=dish,
                    quantity=quantity
                )

        if order.items.exists():
            table.is_occupied = True
            table.save()
            return redirect('order_detail', order_id=order.id)

        order.delete()

    return render(request, 'add_order.html', {
        'table': table,
        'dishes': Dish.objects.all()
    })


def orders(request):
    return render(request, 'orders.html', {
        'orders': Order.objects.all().order_by('-date')
    })


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.status = 'Completed'
        order.save()
        order.table.is_occupied = False
        order.table.save()
        return redirect('orders')

    return render(request, 'order_detail.html', {'order': order})


def table(request):
    return render(request, 'table.html', {
        'tables': Table.objects.all()
    })
