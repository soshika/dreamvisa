from django.shortcuts import render

from .models import Visa


def allvisa(request):
    all_visa = Visa.objects.all()
    return render(request, 'visa/allvisa.html', {'all_visa': all_visa})


def detail(request, visa_id):
    return render(request, 'visa/detail.html')
