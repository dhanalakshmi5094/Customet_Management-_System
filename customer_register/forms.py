from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_id', 'fullname', 'mobile', 'name_title')
        labels = {
            'customer_id': 'Customer ID',
            'fullname': 'Full Name',
            'mobile': 'Mobile Num',
            'name_title': 'Title'
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['name_title'].empty_label = "Select"

