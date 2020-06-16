from django.shortcuts import render
from store.models import Product,Orders

# Create your views here.
def store_view(request):
	my_product  = Product.objects.all()
	context = {
	'pro':my_product
	}
	return render(request,'store.html',context)



def cart_view(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Orders.objects.get_or_create(customer = customer,complete = False)
		items = order.orderitems_set.all()
		print(items)
	else:
		items = []
	context = {
	'item' : items,
	'order':order
	}

	return render(request,'cart.html',context)



def checkout_view(request):
	return render(request,'checkout.html',{})