from django import forms
from coin.models import Coin
from .models import Employee, EmployeeType
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class EmployeeForm(forms.ModelForm):
    category= forms.ModelMultipleChoiceField(
        queryset=EmployeeType.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    #             choices=[(obj,obj) for obj in EmployeeType.objects.all()] )
    # salary_coin= forms.ChoiceField(
    #             choices=[(obj,obj) for obj in Coin.objects.all()] )

    class Meta:
        model = Employee
        fields = ['start_date','category','salary','salary_coin','phone','memo',]
        widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control'}),
          'start_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),

    #         'salary': forms.TextInput(attrs={'class': 'form-control'}),

    #         'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'memo': forms.TextInput(attrs={'row': '20'}),
        }
    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm,self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('name', css_class='form-group col-md-4 mb-0'),
    #             Column('start_date', css_class='form-group col-md-4 mb-0'),
    #             Column('phone', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),

    #         Row(
    #             Column('category', css_class='form-group col-md-4 mb-0'),
    #             Column('salary', css_class='form-group col-md-4 mb-0'),
    #             Column('salary_coin', css_class='form-group col-md-2 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'memo',

    #         Submit('submit','submit')
    #        )


class Employee_TypeForm(forms.ModelForm):

    class Meta:
        model = EmployeeType
        fields = ['category']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'})}
