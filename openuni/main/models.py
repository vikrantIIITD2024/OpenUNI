from django.db import models
from django.contrib import admin

# Create your models here.
COURSE_CATEGORY=[
    ("BACHELORS","BACHELORS"),
    ("MASTERS","MASTERS"),
    ("CERTIFICATE","CERTIFICATE"),
    ("DEGEE","DEGEE"),
    ("PG","PG"),
    ("DIPLOMA","DIPLOMA")
]
FILE_TYPE=[
    ("ASSIGNMENT","ASSIGNMENT"),
    ("QUESTION_PAPER","QUESTION_PAPER"),
    ("WORKBOOK","WORKBOOK"),
    ("EVENTS","EVENTS")
]
from django.contrib.auth.models import User

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100)
    Last_name= models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=100)
    year=models.IntegerField(blank=True)
    
    # Enrollment Number-
    # Regional Centre Code-
    # Regional Centre Name-
    # Study Centre Code-
    # Study Centre Name-
    # Session- Eg. July 2020
    # temporary block
    # permanent block
    # timout
    
class Objects(models.Model):
    coursename = models.CharField(max_length=30,blank=True)
    file_field = models.FileField(upload_to='media/documents/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    course_category=models.CharField(max_length=9,choices=COURSE_CATEGORY,blank=True)
    year=models.IntegerField(blank=True)
    file_type=models.CharField(max_length=15,choices=FILE_TYPE,blank=True)
    
    #2 different pdf for free and paid user
    # paid user pdf view only on mobile app
    
class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'course_category', 'file_type','year')
    
class Payment(models.Model):
    payment_date = models.DateTimeField(auto_now_add=True, blank=True)
    payment_source = models.CharField(max_length=30,blank=True)
    amount=models.IntegerField(blank=True)
    object_name = models.OneToOneField(
        Objects,
        on_delete=models.CASCADE
    )
    user_paid = models.OneToOneField(
        ExtendedUser,
        on_delete=models.CASCADE
    )
    
class PaymentAdmin(admin.ModelAdmin):
    pass
class ExtendedUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(Objects, ObjectsAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(ExtendedUser, ExtendedUserAdmin)
