from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    CheckoutView,
    add_to_cart,
    remove_from_cart,
    OrderSummaryView,
    increase_item_in_cart,
    decrease_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('increase-item-in-cart/<slug>/',
         increase_item_in_cart, name='increase-item-in-cart'),
    path('decrease-item-from-cart/<slug>/', decrease_item_from_cart,
         name='decrease-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

]
