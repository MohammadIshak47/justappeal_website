from django.contrib import admin
from contents.models import Blogs, Gift, OurWork, Gallery,Course

# Register your models here.
admin.site.register(Blogs)
admin.site.register(OurWork)
admin.site.register(Gift)
admin.site.register(Gallery) 
admin.site.register(Course)