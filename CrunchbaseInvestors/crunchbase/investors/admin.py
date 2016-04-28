from django.contrib import admin

from crunchbase.investors.models import People, Investor

admin.site.register(Investor)
admin.site.register(People)
