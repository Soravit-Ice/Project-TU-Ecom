from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name="store"),
    path('store/<str:category>/', views.store, name="store_search"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('', views.landingPage, name="landing_page"),
    path('login/', views.login, name="login"),
    path('shop/', views.shop, name="shop"),
    path('about/', views.about, name="about"),
    path('detail/<int:product_id>', views.detailProduct, name='detail'),
]
