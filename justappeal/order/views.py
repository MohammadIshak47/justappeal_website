from django.shortcuts import render, redirect
# from .models import Order, OrderedItem
from contents.models import Gift
# from core.models import Ticket
from sslcommerz_lib import SSLCOMMERZ

settings = { 'store_id': 'getgu65472ee3b7e7b', 'store_pass': 'getgu65472ee3b7e7b@ssl', 'issandbox': True }
sslcz = SSLCOMMERZ(settings)

def pay_with_sslcz(amount):
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "http://127.0.0.1:8000/"
    post_body['fail_url'] = "your fail url"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "test"
    post_body['cus_email'] = "test@test.com"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "customer address"
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"
    response = sslcz.createSession(post_body)
    return f"{response['GatewayPageURL']}"
    # return f"{response['GatewayPageURL']}"

# def add_to_cart(request, item_id, item_type):
#     if item_type == 'ticket':
#         item = Ticket.objects.get(pk=item_id)
#     elif item_type == 'gift':
#         item = Gift.objects.get(pk=item_id)
#     else:
#         return redirect('donation')  # Redirect to donation page for unknown item types

#     cart = request.session.get('cart', {'items': []})

#     for cart_item in cart['items']:
#         if cart_item['id'] == item_id and cart_item['type'] == item_type:
#             cart_item['quantity'] += 1
#             break
#     else:
#         cart['items'].append({'id': item_id, 'type': item_type, 'quantity': 1})

#     request.session['cart'] = cart
#     return redirect('view_cart')

# def remove_from_cart(request, item_id, item_type):
#     cart = request.session.get('cart', {'items': []})
#     cart['items'] = [item for item in cart['items'] if not (item['id'] == item_id and item['type'] == item_type)]
#     request.session['cart'] = cart
#     return redirect('view_cart')

# def view_cart(request):
#     cart = request.session.get('cart', {'items': []})
#     cart_items = []

#     total_price = 0

#     for cart_item in cart['items']:
#         if cart_item['type'] == 'ticket':
#             item = Ticket.objects.get(pk=cart_item['id'])
#         elif cart_item['type'] == 'gift':
#             item = Gift.objects.get(pk=cart_item['id'])
#         else:
#             continue  # Handle unknown item type

#         subtotal = item.price * cart_item['quantity']
#         total_price += subtotal
#         cart_items.append({'item': item, 'quantity': cart_item['quantity'], 'subtotal': subtotal})

#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

# def order_page(request):
#     if request.method == 'POST':
#         # Get user information from the form
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')

#         # Create an order
#         order = Order.objects.create(
#             name=name,
#             email=email,
#             phone_number=phone_number,
#             total_amount=request.session.get('cart_total', 0)
#         )

#         # Add ordered items to the order
#         cart = request.session.get('cart', {'items': []})
#         for cart_item in cart['items']:
#             quantity = cart_item['quantity']

#             if cart_item['type'] == 'ticket':
#                 ticket = Ticket.objects.get(pk=cart_item['id'])
#                 OrderedItem.objects.create(order=order, ticket=ticket, quantity=quantity)
#             elif cart_item['type'] == 'gift':
#                 gift = Gift.objects.get(pk=cart_item['id'])
#                 OrderedItem.objects.create(order=order, gift=gift, quantity=quantity)

#         # Clear the cart after the order is placed
#         request.session['cart'] = {'items': []}
#         request.session['cart_total'] = 0

#         return render(request, 'order_confirmation.html', {'order': order})

#     cart = request.session.get('cart', {'items': []})
#     total_price = sum(item['quantity'] * item['item'].price for item in cart['items'])
#     request.session['cart_total'] = total_price

#     return render(request, 'order_page.html', {'cart_items': cart['items'], 'total_price': total_price})
