from django.shortcuts import render
from myApp.models import Customer
# Create your views here.
def View1(request):
    c = Customer.objects.all()
    d = {'cust': c}
    return render(request,'myApp/1.html',d)
