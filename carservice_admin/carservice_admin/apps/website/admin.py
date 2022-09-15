from django.contrib import admin
from carservice_admin.apps.website.models.bank_accounts import BankAccounts
from carservice_admin.apps.website.models.person import Person
from carservice_admin.apps.website.models.cities import Cities
from carservice_admin.apps.website.models.provinces import Provinces
from carservice_admin.apps.website.models.employee import Employee

# from carservice_admin.apps.website.models.providers import Providers
# from carservice_admin.apps.website.models.companies import Companies
from carservice_admin.apps.website.models.customer import Customer

# from carservice_admin.apps.website.models.vehicles import Vehicles
# from carservice_admin.apps.website.models.vehicle_owner import VehicleOwner
# from carservice_admin.apps.website.models.budgets import Budget
# from carservice_admin.apps.website.models.repair import Repair
# Register your models here.
admin.site.register(Person)
admin.site.register(BankAccounts)
admin.site.register(Employee)
# admin.site.register(Providers)
# admin.site.register(Companies)
admin.site.register(Customer)
# admin.site.register(Vehicles)
# admin.site.register(VehicleOwner)
# admin.site.register(Budget)
# admin.site.register(Repair)


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    """Cities admin."""

    list_display = ("name",)


@admin.register(Provinces)
class ProvincesAdmin(admin.ModelAdmin):
    """Cities admin."""

    list_display = ("name",)
