"""
URL configuration for OilTraders project.

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
from django.conf.urls.static import static
from OilTraders import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('sales_report/',views.sales_report,name="sales_report"),
    path('generate_report/',views.generate_report,name="generate_report"),
    path('new_entry/',views.new_entry,name="new_entry"),
    path('alertLowProduct/',views.alertLowProduct,name="alertLowProduct"),
    path('sendReminders/',views.sendReminders,name="sendReminders"),
    path('invoice_pdf/<str:pk>/',views.invoice_pdf,name="invoice_pdf"),
    path('bill_pdf/<str:pk>/',views.bill_pdf,name="bill_pdf"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)