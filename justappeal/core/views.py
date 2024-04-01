from django.shortcuts import render, redirect
from core.models import Event, Appeal, Volenture, Donation, TicketSold,GlobalAppeal
from order.views import pay_with_sslcz
from django.core.paginator import Paginator
from django.db.models import Q

# from django.core.mail import send_mail

def appeals(request):
	appeals = Appeal.objects.all()
	context={'appeals': appeals}
	if request.method == "POST":
		appeal_id = request.POST["id"]
		amount = request.POST["amount"]
		amount = int(amount)
		appeal = Appeal.objects.get(id=appeal_id)
		appeal.raised_fund += amount
		appeal.save()
		return redirect(pay_with_sslcz(amount))
	return render(request, 'appeals.html', context)

def appeal_details(request, id):
	appeal = Appeal.objects.get(id=id)
	context = {"appeal": appeal}
	return render(request, "appeal_details.html", context)

def events(request):
	events = Event.objects.all()
	context = {'events': events}
	if request.method == "POST":
		price = request.POST["amount"]
		ev_id = request.POST["id"]
		TicketSold.objects.create(event__id=ev_id, price=price)
		return redirect(pay_with_sslcz(price))
	return render(request, 'events.html', context)

def event_details(request, id):
	event = Event.objects.get(id=id)
	context= {"event": event}
	return render(request, 'event_details.html', context)

def joiner(request, v_type):
	image = request.POST["image"]
	age = request.POST["age"]
	full_name = request.POST["full_name"]
	email = request.POST["email"]
	number = request.POST["num"]
	address = request.POST["address"]
	country = request.POST["country"]
	volenture_type = v_type
	volenture = Volenture.objects.create(
								image=image,age=age,full_name=full_name,
								 address=address, email=email,number=number,
								  country=country, volenture_type=volenture_type)
	return volenture.save()

def volentures(request):
	if request.method == "POST":
		joiner(request, v_type='volentures')
	return render(request, 'volunteers.html')

def adviser(request):
	if request.method == "POST":
		joiner(request, v_type='advisor')
	return render(request, 'adviser.html')

def counsellor(request):
	if request.method == "POST":
		joiner(request, v_type='counsellor')
	return render(request, 'counselor.html')

def volentures_details(request, id=None):
	volenture = Volenture.objects.get(id=id)
	context = {"volenture": volenture}
	return render(request, "volenture_details.html", context)

# def donate(request, amount, donate_type):
# 	donation_type = donate_type
# 	amount = request.POST["amount"]
# 	donate = Donation.objects.create(donation_type=donation_type, amount=amount)
# 	return donate.save()


# def donation(request):
# 	if request.method == "POST":
# 		donation_type = request.POST["donation_type"]
# 		amount = request.POST["amount"]
# 		donate = Donation.objects.create(donation_type=donation_type, amount=amount)
# 		donate.save()
# 	return render(request, 'donate.html')

# send_mail(
#     "Subject here",
#     "Here is the message.",
#     settings.EMAIL_HOST_USER,
#     ["to@example.com"],
#     fail_silently=False,
# )






def global_appeals(request):
	globalappeals = GlobalAppeal.objects.all()
	context={'globalappeals': globalappeals}
	if request.method == "POST":
		appeal_id = request.POST["id"]
		amount = request.POST["amount"]
		amount = int(amount)
		appeal = Appeal.objects.get(id=appeal_id)
		appeal.raised_fund += amount
		appeal.save()
		return redirect(pay_with_sslcz(amount))
	return render(request, 'global_appeal.html', context)
