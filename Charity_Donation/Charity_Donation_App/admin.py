from django.contrib import admin
from Charity_Donation_App.models import User, Category, Institution, Donation

admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)


