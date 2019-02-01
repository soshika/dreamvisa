from django.shortcuts import render, get_object_or_404

from .models import Country
from blog.models import Blog

# python manage.py makemessages -l 'fa'
# python manage.py compilemessages


def home(request):
    last_blogs = Blog.objects.order_by('-id')[:3][::-1]
    last_blogs = reversed(last_blogs)
    four_country = Country.objects.order_by('-id')[:3][::-1]

    return render(request, 'countries/index.html', {'blogs': last_blogs,
                                                    'all_country': four_country})


def allcountries(request):
    countries = Country.objects.all()
    return render(request, 'countries/allcountries.html', {'countries': countries})


def detail(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    return render(request, 'countries/detail.html', {'country': country})
