from django.db import models

# Create your models here.
class Ecomm (models.Model):
	Name=models.CharField(max_length=15)
	Email=models.CharField(max_length=30)

class reg(models.Model):
	name=models.CharField(max_length=15)
	Email=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	confirmPassword=models.CharField(max_length=30)
	userAge=models.CharField(max_length=10, blank=True, null=True)
	userAddress=models.CharField(max_length=1000,blank=True, null=True)
	UserBio=models.TextField(max_length=1000,blank=True, null=True)
	# UserProfile=models.TextField(max_length=1000, blank=True, null=True)
	UserImage=models.ImageField(max_length=1000, blank=True, null=True)
	def __str__(self):
		return self.name

class product(models.Model):
		name=models.CharField(max_length=15)
		Category=models.CharField(max_length=30)
		Price=models.CharField(max_length=8)
		Company=models.CharField(max_length=30)
		def __str__(self):
		    return self.name


class FAQ(models.Model):
	Question=models.TextField()
	Answer=models.TextField()
	def __str__(self):
		return self.Question


class Propage(models.Model):
	name=models.CharField(max_length=15)
	Image=models.ImageField(upload_to="data",blank=True)
	Quantity=models.CharField(max_length=10)
	Price=models.CharField(max_length=12)
	Category=models.CharField(max_length=30)
	description=models.TextField()
	def __str__(self):
		return self.name

class ContactMe(models.Model):
	FirstName=models.CharField(max_length=30)
	LastName=models.CharField(max_length=30)
	Email=models.CharField(max_length=50)
	Message=models.TextField()
	def __str__(self):
		return self.FirstName
class Category(models.Model):
	name=models.CharField(max_length=100,primary_key=True)
	def __str__(self):
		return self.name
class Category_Product(models.Model):
	Category_name=models.ForeignKey(Category, on_delete=models.CASCADE)
	Product_name=models.CharField(max_length=100)
	Product_price=models.CharField(max_length=15)
	Product_quantity=models.CharField(max_length=10)
	Product_image=models.ImageField(max_length=1000)
	Product_description=models.TextField()
	def __str__(self):
		return self.Product_name


class reg(models.Model):
	name=models.CharField(max_length=15)
	Email=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	confirmPassword=models.CharField(max_length=30)
	userAge=models.CharField(max_length=10, blank=True, null=True)
	userAddress=models.CharField(max_length=1000,blank=True, null=True)
	UserBio=models.TextField(max_length=1000,blank=True, null=True)
	# UserProfile=models.TextField(max_length=1000, blank=True, null=True)
	UserImage=models.ImageField(max_length=1000, blank=True, null=True)
	def __str__(self):
		return self.name




class Cart(models.Model):
    user = models.ForeignKey(reg, on_delete=models.CASCADE)  # Link to the user who owns the cart
    product = models.ForeignKey(Category_Product, on_delete=models.CASCADE)  # Link to the product
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product in the cart
    added_at = models.DateTimeField(auto_now_add=True)  # When the product was added to the cart

    def __str__(self):
        return f"{self.user.name}'s cart - {self.product.Product_name}"

    def total_price(self):
        return float(self.product.Product_price) * self.quantity  # Assuming Product_price is stored as a string but represents a float
