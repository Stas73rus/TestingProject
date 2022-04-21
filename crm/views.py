from django.shortcuts import render

from .models import Order

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {
        'list': object_list
    })