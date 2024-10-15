"""
URL configuration for dproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from dproject import views

urlpatterns = [
    path('admin-panel/',admin.site.urls),
    path('', views.homePage ),  
    path('rktrad/', views.rktrad,name='home'),  
    path('spices/', views.spices , name='spices'),
    path('dailyuseditems/',views.dailyuseditems, name='dailyuseditems'),
    path('contactus/',views.contactus, name='contactus'),
    path('billing/',views.billing, name='billing'),
    path('cosmetics/',views.cosmetics, name='cosmetics'),
    path('course/<course>',views.coursedetails),
    path('datag/',views.datag, name= 'datag'),
    path('userf/',views.userf, name='userf'),
    path('submitf/',views.submitf, name='submitf'),
    path('calculator/',views.calculator, name='calculator'),
    path('EvenOdd/',views.EvenOdd, name='EvenOdd'),
    path('marksheet/',views.marksheet, name='marksheet'),
    path('newsdetail/<newsid>',views.newsdetail, name='newsdetail'),
    path('seeproduct',views.seeproduct, name='seeproduct'),
    path('Buyproduct',views.Buyproduct, name='Buyproduct'),
    path('form1',views.form1, name='form1'),
    path('paymentinterface',views.paymentinterface, name='paymentinterface'),
    path('Service',views.Service, name='Service'),
   
    ]

if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
