# Create your models here.
from django.db import models
from datetime import date 
from django.utils import timezone
from .choices import *


class user(models.Model):
    pan = models.CharField(max_length=200,primary_key = True)
    Year_of_filing = models.IntegerField()
    Aadhar = models.IntegerField()
    Mobile_no = models.IntegerField()
    DOB = models.DateField()
    
    #Age = models.IntegerField()
    Fname = models.CharField(max_length=200)
    Mname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    
    @property
    def Age(self):
        return timezone.now().year - self.DOB.year
    
 
    '''class Meta:
        unique_together = (('pan','Year_of_filing'),)'''
        

    def __str__(self):
        return self.pan
    

class tax_on_capital_gain(models.Model):
    Gain_category = models.CharField(max_length = 20, choices = GAIN_CAT )
    Asset_type = models.CharField(max_length=20,choices = ASSET_TYPE)
    Holding_period = models.IntegerField()
    Tax_percentage = models.IntegerField(choices = TAX_PER)
    pan = models.ForeignKey(user, on_delete = models.CASCADE, primary_key = True)

    @property
    def toc(self):
        ao=Capital_gain.objects.all()
        for i in ao:
            if(i.pan==self.pan):
                aa = i.Asset_amount
        if(self.Holding_period>10):
            return (self.Tax_percentage+2)/100*aa
        else:
            return self.Tax_percentage/100*aa
        
    def __str__(self):
        return self.Asset_type

class Income_Tax_Slab(models.Model):
    Age_Category = models.CharField(max_length=20, choices = AGE_CAT)
    Income_Category = models.CharField(max_length = 20, choices = TAP)
    pan = models.ForeignKey(user, on_delete = models.CASCADE,primary_key = True)
    Tax_percentage = models.IntegerField(choices = TAP1)
    #Year_of_filing = models.ForeignKey(user, on_delete = models.CASCADE)

    class Meta:
        unique_together = (('pan',),)
    
    def __str__(self):
        return self.Age_Category


class Salary(models.Model):
    Standard_Deduction =models.IntegerField()
    Special_allowance = models.IntegerField()
    HRA = models.IntegerField( )
    Basic_salary = models.IntegerField( )
    pan = models.ForeignKey(user, on_delete = models.CASCADE, primary_key = True)

    @property
    def totinc(self):
        return self.Special_allowance+self.Standard_Deduction+self.Basic_salary+self.HRA
    @property
    def tottax(self):
        oi = Other_Income.objects.all()
        its = Income_Tax_Slab.objects.all()
        ded = Deduction.objects.all()
        for i in oi:
            if(i.pan== self.pan):
                ot = i.oitot
        for j in its:
            if(j.pan == self.pan):
                tp = j.Tax_percentage
        for d in ded:
            if(d.pan == self.pan):
                de=d.totded1
        return (self.totinc+ot-de)*tp/100
                
        



    '''class Meta:
        unique_together = (('pan','Basic_salary'),)'''

    def __str__(self):
        return self.pan

class Capital_gain(models.Model):
    Asset_amount = models.IntegerField()
    pan = models.ForeignKey(user, on_delete = models.CASCADE,primary_key = True)
    Asset_type = models.CharField(max_length = 20 , choices = ASSET_TYPE )

    '''class Meta:
        unique_together=(('pan','Asset_type'),)'''

    def __str__(self):
        return self.Asset_type


class Deduction(models.Model):
     pan = models.ForeignKey(user, on_delete = models.CASCADE,primary_key = True)
     Life_insurance = models.IntegerField()
     PPF = models.IntegerField()
     NSC = models.IntegerField( )
     Tax_saving_fd = models.IntegerField( )
     Stamp_duty_reg = models.IntegerField( )
     EPF = models.IntegerField( )
     ELSS = models.IntegerField( )

     @property
     def totded1(self):
         return self.Life_insurance+self.PPF+self.NSC+self.Tax_saving_fd+self.Stamp_duty_reg+self.ELSS+self.EPF

     '''class Meta:
         unique_together = (('pan','Life_insurance'),)'''

     '''def __str__(self):
        
        return self.pan'''

class Other_Income(models.Model):
    pan = models.ForeignKey(user, on_delete = models.CASCADE,primary_key = True)
    Savings = models.IntegerField()
    Rent = models.IntegerField()
    FD = models.IntegerField( )
    

    @property
    def oitot(self):
        return self.Savings+self.Rent+self.FD

    class Meta:
        unique_together = (('pan','Savings'),)

    '''def __str__(self):
        return self.pan'''

'''class taxcalc(models.Model):
    pan = models.ForeignKey(user, on_delete = models.CASCADE)
    
    @property
    def totinc(self):'''


    

     
    
    
    
    
    
   
