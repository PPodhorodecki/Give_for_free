from django.shortcuts import render
from django.views import View
from Charity_Donation_App.models import User, Category, Institution, Donation


class LandingPage(View):
    def get(self, request):
        ctx = {}
        donations = Donation.objects.all()
        bags = 0
        for donation in donations:
            bags += donation.quantity
        institutions = Institution.objects.count()
        ctx['bags'] = bags
        ctx['institutions'] = institutions
        return render(request, 'index.html', context=ctx)


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

