from django.contrib import admin
from .models import user, tax_on_capital_gain, Income_Tax_Slab, Salary, Capital_gain, Deduction, Other_Income
#from .serializer import userder

class TutorialAdmin(admin.ModelAdmin):

  list_display = ('pan','Year_of_filing','Aadhar','Mobile_no','DOB','Age',
            'Fname','Mname','Lname','email')

   # formfield_overrides = {
    #    models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
     #   }'''



#admin.site.register(userder)
admin.site.register(user)
admin.site.register(tax_on_capital_gain)
admin.site.register(Income_Tax_Slab)
admin.site.register(Salary)
admin.site.register(Capital_gain)
admin.site.register(Deduction)
admin.site.register(Other_Income)
