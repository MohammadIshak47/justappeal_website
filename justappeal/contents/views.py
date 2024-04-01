from django.shortcuts import render, redirect
from contents.models import OurWork,Blogs,Gift, Gallery, GiftSold,Course,ContactUs
from django.views import View
from core.models import*
from order.views import pay_with_sslcz
from django.db.models import Q
from django.core.paginator import Paginator

def donate(request, donate_type):
    donation_type = donate_type
    amount = request.POST["amount"]
    donate = Donation.objects.create(donation_type=donation_type, amount=amount)
    return donate.save()

def home(request):
    return render(request, 'index.html')
    
def search(request):
    if request.method == 'GET':
        search=request.GET['search']
        print(search)
        a=Appeal.objects.filter(Q (title__icontains=search)|Q (description__icontains=search)|Q(created_date__icontains=search)).distinct()
        paginator = Paginator(a, 3)  # Show 25 contacts per page.
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    return render(request, 'search.html',{'search':search,'page_obj':page_obj})


def blogs(request):
    blogs=Blogs.objects.all()
    return render(request,'blog.html',{'blogs':blogs})

def blog_details(request, id=None):
    blog = Blogs.objects.get(id=id)
    context = {'blog': blog}
    return render(request, 'blog_details.html', context)

def gifts(request):
    gifts=Gift.objects.all()
    if request.method == "POST":
        amount = request.POST['amount']
        gift_id = request.POST['id']
        GiftSold.objects.create(gift__id=gift_id, amount=amount)
        return redirect(pay_with_sslcz(amount))
    return render(request,'gift_cards.html',{'gifts':gifts})

def work_details(request, id=None):
    work = OurWork.objects.get(id=id)
    context = {'work':work}
    return render(request, "gits_details.html", context)


def our_works(request):
    our_works =OurWork.objects.all()
    return render(request,'our_work.html',{'our_works':our_works})

def zakat(request):
    if request.method == "POST":
        donate(request, "zakat")
        amount = request.POST["amount"]
        return redirect(pay_with_sslcz(amount))
    return render(request, 'zakat.html')

def sadaqah(request):
    if request.method == "POST":
        donate(request, "sadaqah")
        amount = request.POST["amount"]
        return redirect(pay_with_sslcz(amount))
    return render(request, 'sadaqah.html')

def gallery(request):
    gallery_images = Gallery.objects.all()
    context = {'images': gallery_images }
    return render(request, 'gallery.html', context=context)

def about(request):
    return render(request, 'about_us.html')

def career(request):
    return render(request, 'career.html')



def whyjustappeal(request):
    return render(request, 'why_justappeal.html')


def financial_information(request):
    return render(request,'financialinfo.html')

def faq(request):
    return render(request,'faq.html')

def courses(request):
    courses = Course.objects.all()
   
    return render(request, 'courses.html', {'courses': courses})


class ContactUsView(View):
    def get(self,request):
        return render(request,'contact_us.html')
    def post(self,request):
        if request.method =='POST':
            name = request.POST['name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            message = request.POST['message']
            
            contactus = ContactUs.objects.create(name=name,email=email,mobile_number=mobile_number,message=message)
            contactus.save()
            return redirect('/')
        
 