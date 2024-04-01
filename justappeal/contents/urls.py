from django.urls import path
from contents.views import *

urlpatterns = [
    path('', home, name='home'),
    path('blogs',blogs,name='blogs'),
    path('our_works',our_works,name='our_works'),
    path('OurWorks/<int:id>/', work_details, name="work_details"),
    path('gifts',gifts,name='gifts'),
    path('BlogDetails/<int:id>/', blog_details, name='blog_details'),
    path('zakat',zakat,name='zakat'),
    path('sadaqah',sadaqah,name='sadaqah'),
    path('Gallery/', gallery, name='gallery'),
    path('About/', about, name="about"),
    path('Career/', career, name='career'),
    path('contact_us',ContactUsView.as_view(),name='contact_us'),
    path('search',search,name='search'),
    path('why_justappeal/',whyjustappeal,name='whyjustappeal'),
    path('financialinfo/',financial_information,name='financialinfo'),
    path('faq/',faq,name='faq'),
    path('courses',courses,name='courses'),
]
