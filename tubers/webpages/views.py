from django.shortcuts import render
from webpages.models import Slider,Team
from youtubers.models import Youtuber
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.filter(is_featured = True).order_by('-created_date')
    all_tubers = Youtuber.objects.order_by('-created_date')[:9]
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'all_tubers': all_tubers,
    }
    return render(request, "webpages/home.html",data)

def about(request):
    return render(request, "webpages/about.html")

def services(request):
    return render(request, "webpages/services.html")

def contact(request):
    return render(request, "webpages/contact.html")

