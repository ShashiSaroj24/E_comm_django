from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from myapp.models import *

# Create your views here.
def log(request):
	if request.method=="POST":
		print("enter if")
		e=request.POST.get('em')
		p=request.POST.get('pw')
		expert=reg.objects.filter(Email=e,password=p)
		k=len(expert)
		if k>0:
			request.session['Email']=e
			#return render(request,'Change Password.html',{})
			return render(request,'Contactme.html')
		else:
			return render(request,'Login.html',{'msg':"Invalid User"})
	else:
		print("else part")
		return render(request,"Login.html")
	


def register(request):
	
	if 	request.method=="POST":
		n=request.POST.get('nm')
		e=request.POST.get('em')
		p=request.POST.get('pw')
		c=request.POST.get('cpw')
		# This is the working to make it so that the data that the user types will be stored.
		if p==c:
			if reg.objects.filter(Email=e).exists():
				return render(request,'Register.html',{'msg':"Email Id already exists"})
			else:
				x=reg()
				x.name=n
				x.Email=e
				x.password=p
				x.confirmPassword=c
				x.save()
				return render(request, 'Register.html',{'msg':"User successfully registered"})
		else:
			return render(request,'Register.html',{'msg':"Password and ConfirmPassword does not match"})
	return render(request,'Register.html')		

def frgot(request):
	if(request.method=='POST'):
		e=request.POST.get('e')
		print(e)
		user=reg.objects.filter(Email=e)
		if(len(user)>0):
			p=user[0].password
			subject="Password"
			message="Welcome! your password is"+p
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[e]
			send_mail(subject,message,email_from,recipient_list)
			rest='Your Password sent to your respective Email Account. Please Check it'
			x=Category.objects.all()
		
			return render(request,'Forgot.html',{'rest':rest,'navdata':x})
		else:
			rest='This Email ID is not registered'
			x=Category.objects.all()
			
			return render(request,'Forgot.html',{'rest':rest,'navdata':x})

	else:
		print("else page")
		x=Category.objects.all()
		
		return render(request,'Forgot.html',{'navdata':x})

def foot(request):
	return render(request,'Footer.html')

def getus(request):
	if 	request.method=="POST":
		n=request.POST.get('fn')
		l=request.POST.get('ln')
		e=request.POST.get('ea')
		ma=request.POST.get('m')
		y=ContactMe()
		y.FirstName=n
		y.LastName=l
		y.Email=e
		y.Message=ma
		y.save()
		x=Category.objects.all()
		
		return render(request, 'Contactme.html',{'msg':"Message successfully Sent",'navdata':x})
	else:
		x=Category.objects.all()
		
		return render(request,'Contactme.html',{'navdata':x})	


def change(request):
	if 	request.method=="POST":
		user=reg.objects.get(Email=request.session['Email'])
		OldPassword=request.POST.get('opw')
		NewPassword=request.POST.get('npw')
		ConfirmPassword=request.POST.get('pw')
		if(NewPassword==ConfirmPassword):
			pa=user.password
			print(pa)
			if(OldPassword==pa):
				user.password=NewPassword
				user.confirmPassword=NewPassword
				user.save()
				
				return render(request,'Change_pass.html',{'msg':'Password Changed'})
			else:
				
				return render(request,'Change_pass.html',{'msg':"Invalid Current Passsword"})
				
		else:

			return render(request,'Change_pass.html',{'msg':"Password and c-pass does not match"})
	else:
		return render(request, 'Change_pass.html')

def sidebar(request):
	return render(request,'Sidebar.html')

def review(request):	
	return render(request,'review.html')

def products(request):
	x=Category.objects.all()
	r=product.objects.all()
	
	return render(request,'AllProducts.html',{"data":r,'navdata':x})

def faqs(request):
	y=FAQ.objects.all()
	x=Category.objects.all()
	
	return render(request,'FAQ.html',{"QA":y,'navdata':x})

def Propages(request):
	x=Category.objects.all()
	z=Propage.objects.all()

	return render(request,'Propage.html',{"Details":z,'navdata':x})

# The detailed Products 
def DetP(request, id):
	x=Category.objects.all()
	w=Propage.objects.get(id=id)
	return render(request,'Detail_Product.html',{"data":w,'navdata':x})

# User Profile
def ProU(request):
	user=reg.objects.get(Email=request.session['Email'])
	return render(request,"UserProfile.html",{'user':user})

# def Edit(request):
#   user=reg.objects.get(Email=request.session['Email'])
#   if request.method=='POST':

#   	user.Name = request.POST.get('name')
#   	user.userAge = request.POST.get('AGE')
#   	user.userAddress = request.POST.get('HC')
#   	user.UserBio = request.POST.get('Bo')
#   	user.UserImage = request.FILES['profile']
#   	user.save()
#   	return redirect('/User')
#   else:
#   	return render(request,"EditProfile.html",{'user' :user})

def logout(request):
	if not request.session.has_key('Email'):
		return redirect('/login')
	del request.session['Email']
	return redirect('/login')

def nav(request):
	x=Category.objects.all()

	return render(request,'Navbar.html',{'navdata':x})

def ProCat(request, name):
	x=Category.objects.all()
	O=Category_Product.objects.filter(Category_name=name)

	return render(request,'Product_cat.html',{"cate":O,'navdata':x})
# Detailed Product Part-2
def index(request):
	c=Category_Product.objects.all()
	return render(request,'index.html',{'data':c})
def DePe(request, id):
	x=Category.objects.all()
	c=Category_Product.objects.get(id=id)
	return render(request,'Cat_Pro.html',{"cast":c,'navdata':x})

def Addcar(request):
	return render(request,'Add_Cart.html')	

def ship(request):
	return render(request,'Shippin.html')


def add_to_cart(request):
	if request.method=="POST":
		print("working")

		user_data=reg.objects.get(Email=request.session['Email'])
		user=user_data
		product_id=request.POST.get('product_id')
		product=Category_Product.objects.get(id=product_id)
		Cart(user=user, product=product).save()
		print("--------------working-------------")
		return redirect('/Cart')

def Addcar(request):
	user_data=reg.objects.get(Email=request.session['Email'])
	user=user_data
	all_data=Cart.objects.filter(user=user)
	amount=0
	for i in all_data:
		product_price = i.product.Product_price.replace(',', '')
		single_cost = int(i.quantity) * int(product_price)  # Convert to int after removing commas
		amount += single_cost
	total_amount=amount+40 #40 rs. is a shipping charges
	return render(request,'Add_Cart.html',{'cart_data':all_data, 'total_amount':total_amount,'amount':amount})	



def decrement_quantity(request, id):
	if request.method=="POST":
		print("enter")
		user_data=reg.objects.get(Email=request.session['Email'])
		cart_data = get_object_or_404(Cart, id=id, user=user_data)
		print(cart_data)
		print(cart_data.quantity)
		if cart_data.quantity >1:
			cart_data.quantity-=1
			if cart_data.quantity==0:
				cart_data.delete()

			cart_data.save()
		else:
			cart_data.delete()
		
		print("-------------data decrement--------")
		return redirect('/Cart')


def Increment_quantity(request, id):
	if request.method=="POST":
		print("enter")
		user_data=reg.objects.get(Email=request.session['Email'])
		cart_data = get_object_or_404(Cart, id=id, user=user_data)
		
		
		cart_data.quantity+=1
		cart_data.save()
		
		print("-------------data decrement--------")
		return redirect('/Cart')

