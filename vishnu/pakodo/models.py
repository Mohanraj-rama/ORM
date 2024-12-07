from django.db import models
from django.contrib import admin
class Loan(models.Model):
   Customerid=models.CharField(max_length=20, primary_key=True)
   Customername=models.CharField(max_length=100)
   Mobile=models.IntegerField( )
   Age=models.IntegerField( )
   Email=models.EmailField( )
   DOB=models.DateField( )
   Loan_amount=models.IntegerField( )
class LoanAdmin(admin.ModelAdmin):
    list_display=('Customerid','Customername','Mobile','Age','Email','DOB','Loan_amount')
