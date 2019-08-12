from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import user, tax_on_capital_gain, Income_Tax_Slab, Salary, Capital_gain, Deduction, Other_Income


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    '''def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user'''


class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
class tocgform(forms.ModelForm):
    
    class Meta:
        
        model = tax_on_capital_gain
        fields = [
            'Gain_category','Asset_type','Holding_period','Tax_percentage','pan']

        
'''class tocgform123(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pan'].queryset = user.objects.all()
    Gain_category = forms.CharField()
    Asset_type = forms.CharField()
    Holding_period = forms.CharField()
    Tax_percentage = forms.CharField()
    pan = forms.ModelChoiceField(queryset = user.objects.all())'''
    
class Itsform(forms.ModelForm):
    class Meta:
        model = Income_Tax_Slab
        fields = ['Age_Category','Income_Category','Tax_percentage','pan']

class Salaryform(forms.ModelForm):

    class Meta:
        model = Salary
        fields = ['Standard_Deduction','Special_allowance','HRA','Basic_salary','pan']
        
        
class cgform(forms.ModelForm):
    class Meta:
        model = Capital_gain
        fields = '__all__'

class deductionform(forms.ModelForm):
    class Meta:
        model = Deduction
        fields = ['pan','Life_insurance','PPF','NSC','Tax_saving_fd','Stamp_duty_reg','EPF','ELSS']

class oiform(forms.ModelForm):
    class Meta:
        model = Other_Income
        fields=['pan','Savings','Rent','FD']
