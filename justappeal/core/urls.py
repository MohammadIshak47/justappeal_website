from django.urls import path
from core.views import *
urlpatterns = [
	path('Volentures/', volentures, name="volentures"),
	path("VolentureDetails/", volentures_details, name="volenture_details"),
	path("Events/", events, name="events"),
	path("EventDetails/", event_details, name="evet_details"),
	path("Appeals/", appeals, name="appeals"),
    path("global_appeals/",global_appeals,name='globalappeals'),
	path("AppealDetails/", appeal_details, name="appeal_details"),
	# path('Donation/', donation, name="donate"),
	path('Advisor/', adviser, name='adviser'),
	path('Counsellor', counsellor, name='counsellor'),
	
]
