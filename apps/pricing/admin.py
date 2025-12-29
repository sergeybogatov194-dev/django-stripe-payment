from django.contrib import admin

from .models import Discount, Tax

admin.site.register(Discount)
admin.site.register(Tax)