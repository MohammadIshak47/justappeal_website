from django.urls import path
from .views import pay_with_sslcz

urlpatterns = [
    # path('add_to_cart/<int:item_id>/<str:item_type>/', add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<int:item_id>/<str:item_type>/', remove_from_cart, name='remove_from_cart'),
    # path('view_cart/', view_cart, name='view_cart'),
    path('PayNow/', pay_with_sslcz, name='pay_now'),
    # path('order_page/', order_page, name='order_page'),
]