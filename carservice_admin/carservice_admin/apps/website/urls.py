# Django
from django.urls import path

# Views
from carservice_admin.apps.website.views.customers_views import (
    CustomerView,
    CustomerDetailView,
    CustomerDelete,
    CustomerCreate,
    CustomerCreateBusiness,
    CustomerUpdateBusinessView,
)

urlpatterns = [
    path("customers/", CustomerView.as_view(), name="customer_list"),
    path("customers/create/", CustomerCreate.as_view(), name="customer_create"),
    path(
        "customers/create/business",
        CustomerCreateBusiness.as_view(),
        name="customer_create_business",
    ),
    path(
        "customers/<pk>/update/",
        CustomerUpdateBusinessView.as_view(),
        name="customer_update_business",
    ),
    path("customers/<int:id>/edit", CustomerDetailView.as_view(), name="customer_edit"),
    path("customers/<pk>/delete/", CustomerDelete.as_view(), name="customer_delete"),
]
