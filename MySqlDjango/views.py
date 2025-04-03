from django.db.models import Q
from django.shortcuts import render
from MySqlDjango.models import Customer, Order

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer.html", {"customers": customers})
def order_list(request):
    orders = Order.objects.select_related("customer").all()
    return render(request, "orders.html", {"orders": orders})


def search_orders(request):
    query = request.GET.get("q", "").strip()
    orders = []

    if query:
        search_parts = query.split()
        if len(search_parts) == 2:
            first_name, last_name = search_parts
            orders = Order.objects.filter(
                customer__first_name__icontains=first_name,
                customer__last_name__icontains=last_name
            )
        else:
            orders = Order.objects.filter(
                Q(customer__first_name__icontains=query) | Q(customer__last_name__icontains=query)
            )

    return render(request, "search_orders.html", {"list_of_all_orders": orders, "query": query})
