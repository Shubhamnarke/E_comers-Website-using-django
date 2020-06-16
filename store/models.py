from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Customer(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE,blank = True,null = True)
	name = models.CharField(max_length =100 , null = True)
	email = models.CharField(max_length =100 , null = True)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length =200,null = True)
	price = models.FloatField()
	digital = models.BooleanField(default = False,blank = True,null = True)
	image = models.ImageField(blank = True,null = True)


	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url =  self.image.url
		except:
			url = ''

		return url
	

total_list = []
class Orders(models.Model):
	customer = models.ForeignKey(Customer,on_delete = models.SET_NULL ,null = True)
	date_posted = models.DateTimeField(auto_now_add = True)
	complete = models.BooleanField(default = False,blank = True,null = True)
	transaction_id = models.CharField(max_length =200,null = True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitems_set.all()
		final = sum([item.get_total for item in orderitems])
		return final

	@property
	def get_cart_item(self):
		orderitems = self.orderitems_set.all()
		final = sum([item.quantity for item in orderitems])
		return final
			


class OrderItems(models.Model):
	product = models.ForeignKey(Product,on_delete = models.SET_NULL ,blank = True ,null = True)
	order = models.ForeignKey(Orders,on_delete = models.SET_NULL ,blank = True,null = True)
	quantity = models.IntegerField(default = 0,null = True,blank = True)
	date_added = models.DateTimeField(auto_now_add = True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		total_list.append(total)
		return total
	

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer,on_delete = models.SET_NULL ,blank = True ,null = True)
	order = models.ForeignKey(Orders,on_delete = models.SET_NULL ,blank = True ,null = True)
	address = models.CharField(max_length = 200,null =False)
	city = models.CharField(max_length = 200,null =False)
	zip_code = models.CharField(max_length = 200,null =False)
	mobile = models.CharField(max_length = 200,null =False)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.address