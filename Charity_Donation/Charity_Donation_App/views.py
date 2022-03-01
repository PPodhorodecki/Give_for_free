from django.shortcuts import render, redirect
from django.views import View
from Charity_Donation_App.models import User, Category, Institution, Donation
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout

class LandingPage(View):
    def get(self, request):
        ctx = {}
        donations = Donation.objects.all()
        bags = 0
        for donation in donations:
            bags += donation.quantity
        ins_val = Institution.objects.count()
        ctx['bags'] = bags
        ctx['ins_val'] = ins_val
        ins_f = Institution.objects.filter(type=1)
        ins_o = Institution.objects.filter(type=2)
        ins_l = Institution.objects.filter(type=3)
        # ctx['ins_f'] = ins_f
        # ctx['ins_o'] = ins_o
        # ctx['ins_l'] = ins_l
        paginator_f = Paginator(ins_f, 2)
        paginator_o = Paginator(ins_o, 2)
        paginator_l = Paginator(ins_l, 2)
        page_f = request.GET.get('page')
        institutions_f = paginator_f.get_page(page_f)
        page_o = request.GET.get('page')
        institutions_o = paginator_o.get_page(page_o)
        page_l = request.GET.get('page')
        institutions_l = paginator_l.get_page(page_l)
        ctx['institutions_f'] = institutions_f
        ctx['institutions_o'] = institutions_o
        ctx['institutions_l'] = institutions_l
        return render(request, 'index.html', context=ctx)


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return redirect('/register')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST.get('name')
        last_name = request.POST.get('surname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password2')
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = email
        user.set_password(pass1)
        user.save()
        return redirect('/login')

