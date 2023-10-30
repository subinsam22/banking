from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
Account_choices = (('savings', 'Savings Account'),
    ('fixed', 'Fixed Account'),
    ('NRI', 'NRI Account'),)
DISTRICT_CHOICES = (('ernakulam','Ernakulam'),('kollam','Kollam'),('Kottayam','Kottayam'),('idukki','Idukki'),('thrissur','Thrissur'))

Materials_choices = (('Debit', 'Debit Card'),
    ('Credit', 'Credit Card'),
    ('Cheque', 'Cheque Book'),)

class District(models.Model):
    name = models.CharField(max_length=20)
    def __str__ (self):

        return self.name
class Branch(models.Model):
    name = models.CharField(max_length=20)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__ (self):

        return self.name
class application(models.Model):
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    email = models.CharField(max_length=128)
    DOB = models.DateField()
    age = models.IntegerField()
    phone_number = models.IntegerField()
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    account_type = models.CharField(max_length=10,choices=Account_choices)
    debit=models.BooleanField(blank=True,default=False,null=True)
    credit = models.BooleanField(blank=True,default=False,null=True)
    cheque = models.BooleanField(blank=True,default=False,null=True)
    application_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    def __str__ (self):

        return self.name

    class Meta:
        ordering = ['created']



