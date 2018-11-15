from django.shortcuts import render,get_object_or_404
from . import models
# Create your views here.
def product_detail(request,pk):
	product=get_object_or_404(models.Product,pk=pk)
	return render(request,'product_detail.html',{'product':product})
