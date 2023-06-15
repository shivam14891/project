from . views import UserViewSet
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from.import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [

    path("", views.index, name="home"),
    path('signup', views.signup, name="sign"),
    path('login', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('cart/', views.cart_details, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('orders/', views.order, name="order"),
    path('rest/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
