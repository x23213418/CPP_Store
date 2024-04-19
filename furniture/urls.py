"""
URL configuration for furniture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('product/<id>/', views.product, name='product'),
    path('login/', views.login, name='login'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('signup/', views.signup, name='signup'),
    path('handle_signup/', views.handle_signup, name='handle_signup'),
    path('logout/', views.logout, name='logout'),
    path('order_now/', views.order_now, name='order_now'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('edit_order/', views.edit_order, name='edit_order'),
    path('handle_edit_order/', views.handle_edit_order, name='handle_edit_order'),
    path('delete_order/', views.delete_order, name='delete_order'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)