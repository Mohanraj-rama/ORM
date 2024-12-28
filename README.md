# Ex02 Django ORM Web Application
# Date:2.12.2024
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
### admin.py
```
from django.contrib import admin
from .models import Loan,LoanAdmin
admin.site.register(Loan,LoanAdmin)
```
### models.py
```
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

```
# OUTPUT
![WhatsApp Image 2024-12-07 at 10 48 41 PM](https://github.com/user-attachments/assets/65e9e71a-6c8e-4da4-959e-715097a2981a)
![Screenshot (82)](https://github.com/user-attachments/assets/fe0a7d5f-cef7-41c5-b70f-987035a6db4a)
![Screenshot (81)](https://github.com/user-attachments/assets/68f35d48-6fbe-4037-ad2c-93e0ccea3b12)



# RESULT
Thus the program for creating a database using ORM hass been executed successfully
