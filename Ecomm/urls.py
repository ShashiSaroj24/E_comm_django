"""
URL configuration for Ecomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", views.log , name="login"),
    path("reg", views.register , name="reg"),
    path("frgot", views.frgot , name="forgot"),
    path("foot", views.foot , name="foot"),
    path("contact",views.getus , name="contact"),
    path("change",views.change , name="change"),
    path("sidebar",views.sidebar , name="sidebar"),
    path("review",views.review, name="review"),
    path("products",views.products, name="products"),
    path("FAQ",views.faqs, name="FAQ"),
    path("Propage",views.Propages, name="Propage"),
    path("DProduct/<int:id>",views.DetP, name="DProduct"),
    path("User",views.ProU, name="User"),
    path("",views.index, name="index"),
    # path("Edit",views.Edit, name="Edit"),
    path("logout",views.logout, name="logout"),
    path("NavB",views.nav,name="NavB" ),
    path("Prece/<str:name>",views.ProCat,name="Prec"),
    path("DeProduct/<int:id>",views.DePe, name="DeProduct"),
    path("ProShip",views.ship,name="Shippin"),
    path("Cart",views.Addcar,name="Cart"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("decrement_quantity/<int:id>", views.decrement_quantity, name="decrement_quantity"),
    path("Increment_quantity/<int:id>", views.Increment_quantity, name="Increment_quantity"),
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)