from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100,blank=True)
    Last_name= models.CharField(max_length=100,blank=True)
    Gender = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    Phone_number = models.CharField(max_length=100,blank=True)
    year=models.IntegerField(blank=True)
    Enrollment_Number = models.CharField(max_length=100,blank=True)
    Regional_Centre_Code = models.CharField(max_length=100,blank=True)
    Regional_Centre_Name = models.CharField(max_length=100,blank=True)
    Study_Centre_Code = models.CharField(max_length=100,blank=True)
    Study_Centre_Name = models.CharField(max_length=100,blank=True)
    Session = models.CharField(max_length=100,blank=True)
    temporary_block = models.BooleanField(default=False)
    permanent_block = models.BooleanField(default=False)
    timout = models.DateTimeField(blank=True)
    
class Objects(models.Model):
    coursename = models.CharField(max_length=30,blank=True)
    # free_user_file = models.FileField(upload_to='media/documents/free/',blank=True)
    # paid_user_file = models.FileField(upload_to='media/documents/paid/',blank=True)
    paid_user_file = CloudinaryField(resource_type="auto", null=True, blank=True)
    free_user_file = CloudinaryField(resource_type="auto", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    course_category=models.CharField(max_length=9,choices=COURSE_CATEGORY,blank=True)
    year=models.IntegerField(blank=True)
    file_type=models.CharField(max_length=15,choices=FILE_TYPE,blank=True)
    
class Events(models.Model):
    event_name = models.CharField(max_length=30,blank=True)
    event_date = models.DateTimeField(blank=True)
    
    
class FAQ(models.Model):
    question = models.CharField(max_length=200,blank=True)
    answer = models.CharField(max_length=1000,blank=True)
    
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
    list_display=('email','Phone_number','year','First_name')
    search_fields = ('email', 'Phone_number','Enrollment_Number')
    
class EventsAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date')
    pass

class FAQAdmin(admin.ModelAdmin):
    pass


admin.site.register(Objects, ObjectsAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(ExtendedUser, ExtendedUserAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(FAQ, FAQAdmin)
