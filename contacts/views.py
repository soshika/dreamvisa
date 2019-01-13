from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone


def contact(request):
    return render(request, 'contact.html', {})
