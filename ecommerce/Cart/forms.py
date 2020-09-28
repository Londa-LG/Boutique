from django import forms

from .models import BillingDetails


class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingDetails
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'company_name',
            'country',
            'address_line1',
            'address_line2',
            'town_or_city',
            'state_or_country'
        ]

