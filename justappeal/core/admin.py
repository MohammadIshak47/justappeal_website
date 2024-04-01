from django.contrib import admin
from core.models import Appeal, Event, Volenture, Donation,GlobalAppeal
# Register your models here.
admin.site.register(Event)
admin.site.register(Appeal)
admin.site.register(Volenture)
admin.site.register(Donation)
admin.site.register(GlobalAppeal)