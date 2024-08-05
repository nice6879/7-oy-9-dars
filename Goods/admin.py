from django.contrib import admin
from . import models
from .models import Borrower, Loan, Payment, LoanOfficer

admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductImg)
admin.site.register(models.Cart)
admin.site.register(models.CartProduct)
admin.site.register(models.Order)

# myapp/admin.py

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'amount', 'interest_rate', 'term', 'start_date', 'end_date', 'status')
    search_fields = ('borrower__first_name', 'borrower__last_name')
    list_filter = ('status', 'start_date')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'payment_date', 'amount', 'method')
    search_fields = ('loan__borrower__first_name', 'loan__borrower__last_name')
    list_filter = ('payment_date', 'method')

@admin.register(LoanOfficer)
class LoanOfficerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')
