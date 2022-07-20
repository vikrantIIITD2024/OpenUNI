from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Max
from import_export.admin import ExportActionMixin

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

IMG_CATEGORY=[
    ("SLIDER","SLIDER"),
    ("ABOUT","ABOUT"),
]

class ExtendedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True)
    course = models.CharField(max_length=100,blank=True)
    email = models.CharField(max_length=100,blank=True)
    Phone_number = models.CharField(max_length=100,blank=True)
    # year=models.IntegerField(blank=True,null=True)
    Enrollment_Number = models.CharField(max_length=100,blank=True)
    Regional_Centre_Code = models.CharField(max_length=100,blank=True)
    Regional_Centre_Name = models.CharField(max_length=100,blank=True)
    Study_Centre_Code = models.CharField(max_length=100,blank=True)
    Study_Centre_Name = models.CharField(max_length=100,blank=True)
    Session = models.CharField(max_length=100,blank=True)
    temporary_block = models.BooleanField(default=False)
    permanent_block = models.BooleanField(default=False)
    timeout = models.DateTimeField(blank=True,null=True)
    profile_img = CloudinaryField(resource_type="auto", null=True, blank=True)
    dob = models.DateTimeField(blank=True,null=True)
class Courses(models.Model):
    name=models.CharField(max_length=100)
class Objects(models.Model):
    coursename = models.CharField(max_length=100,blank=True)
    
    paid_user_file = CloudinaryField(resource_type="auto", null=True, blank=True)
    free_user_file = CloudinaryField(resource_type="auto", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    course_category=models.CharField(max_length=20,choices=COURSE_CATEGORY,blank=True)
    year=models.IntegerField(blank=True)
    file_type=models.CharField(max_length=15,choices=FILE_TYPE,blank=True)
    price=models.IntegerField(blank=True)
    thumbnail = CloudinaryField(resource_type="auto", null=True, blank=True)
    course_id = models.CharField(max_length=100) 
    # coursename=models.ForeignKey(
    #     Courses,
    #     on_delete=models.CASCADE
    # ) 

    def save(self, **kwargs):
        if not self.course_id:
            max = Objects.objects.aggregate(id_max=Max('id'))['id_max']
            self.course_id = "{}{:05d}".format('OU', max if max is not None else 1)
        super().save(*kwargs)
        
    def __str__(self):
        return self.course.name

class Session(models.Model):
    name=models.CharField(max_length=100)
    
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Events(models.Model):
    event_name = models.CharField(max_length=100,blank=True)
    event_date = models.DateTimeField(blank=True)
    
class Images(models.Model):
    image= CloudinaryField(resource_type="auto", null=True, blank=True)
    category=models.CharField(max_length=9,choices=IMG_CATEGORY,blank=True)
    redirect_link= models.CharField(max_length=100)  
    
class FAQ(models.Model):
    question = models.CharField(max_length=200,blank=True)
    answer = models.CharField(max_length=1000,blank=True)
    
class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'course_category', 'file_type','year')
    list_filter = ('coursename', 'course_category', 'file_type','year')
    
class Payment(models.Model):
    payment_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_date = models.DateTimeField(blank=True,null=True)
    method = models.CharField(max_length=100,blank=True)
    amount=models.IntegerField(blank=True)
    payment_source= models.CharField(max_length=100,null=True,blank=True,editable=False)
    order_id= models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100,null=True,blank=True)
    bank=models.CharField(max_length=100,null=True,blank=True)
    wallet=models.CharField(max_length=100,null=True,blank=True)
    vpa=models.CharField(max_length=100,null=True,blank=True)
    error_code=models.CharField(max_length=100,null=True,blank=True)
    error_description=models.CharField(max_length=100,null=True,blank=True)
    error_source=models.CharField(max_length=100,null=True,blank=True)
    error_step=models.CharField(max_length=100,null=True,blank=True)
    error_reason=models.CharField(max_length=100,null=True,blank=True)
    
    object_name = models.ForeignKey(
        Objects,
        on_delete=models.CASCADE
    )
    user_paid = models.ForeignKey(
        ExtendedUser,
        on_delete=models.CASCADE
    )
    
class PaymentAdmin(admin.ModelAdmin):
    list_display=('payment_date','method','amount','order_id','status')   
    list_filter=('status','payment_date')
    pass

class ImagesAdmin(admin.ModelAdmin):
    list_display=('image','category')

class ExtendedUserAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=('email','Phone_number','name')
    search_fields = ('email', 'Phone_number','Enrollment_Number','name')
    
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
admin.site.register(Images, ImagesAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Session, SessionAdmin)