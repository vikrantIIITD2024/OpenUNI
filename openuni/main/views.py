from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main.models import *
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from datetime import datetime
import razorpay
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt    


RZP_SECRET='dPr5X1NULK7VXJapgUvJRbvo'
client = razorpay.Client(auth=("rzp_test_Gp2RtcpeNCmGOL",RZP_SECRET))
client.set_app_details({"title" : "OpenUni", "version" : "1.0"})

PAGE_DATA={
    'assignments':{
        'title':'Assignments - OpenUni',
        'h1':'Solved Assignments'
    },
    'courses':{
        'title':'Courses - OpenUni',
        'h1':'Courses'
    },
    'bachelors':{
        'title':'Bachelors - OpenUni',
        'h1':'Bachelors'
    },
    'masters':{
        'title':'Masters - OpenUni',
        'h1':'Masters'
    },
    'certificate':{
        'title':'Certificate - OpenUni',
        'h1':'Certificate'
    },
    'degree':{
        'title':'Degree Program - OpenUni',
        'h1':'Degree Program'
    },
    'pg':{
        'title':'PG Program - OpenUni',
        'h1':'PG Program'
    },
    'diploma':{
        'title':'Diploma - OpenUni',
        'h1':'Diploma'
    },
    'assignment':{
        'title':'Assignments - OpenUni',
        'h1':'Assignments'
    },
    'question_paper':{
        'title':'Question Papers - OpenUni',
        'h1':'Question Papers'
    },
    'workbook':{
        'title':'Workbook - OpenUni',
        'h1':'Workbook'
    },
    'events':{
        'title':'Events - OpenUni',
        'h1':'Events'
    }
}


def handler404(request, *args, **argv):
    return {'msg':'url not found'}

def index(request):
    images=Images.objects.filter(category='SLIDER')
    about_img=Images.objects.filter(category='ABOUT')[0].image.url
    img_data=[]
    objs=Objects.objects.all()
    
    data=[]
    for obj in objs:
        data.append({
            'coursename': obj.coursename,
            'price':obj.price,
            'course_category':obj.course_category,
            'file_type':obj.file_type,
            'thumbnail':obj.thumbnail.url,
            'course_id':obj.course_id,
        })
    for img in images:
        img_data.append({
            'img_link':img.image.url,
            'redirect_link':img.redirect_link
        })
    return render(request, 'index.html',{'images':img_data,'about_img':about_img,'data':data})

def courses(request):
    path=request.get_full_path().split('/')[1]
    path=path.split('?')[0]
    page_data=PAGE_DATA[path]
    
    
    type=request.GET.get('type')
    year=request.GET.get('year')
    category=request.GET.get('course_category')
    coursename=request.GET.get('coursename')
    
    key='courses'
    if type:key=type
    if category:key=category
    
    # print(key)
    page_data=PAGE_DATA[key.lower()]
    
    
    if type and category and year:
        objs=Objects.objects.filter(file_type=type,year=year,course_category=category)
    elif type and category:
        objs=Objects.objects.filter(file_type=type,course_category=category)
    elif type and year:
        objs=Objects.objects.filter(file_type=type,year=year)
    elif year and category:
        objs=Objects.objects.filter(year=year,course_category=category)
    elif type:
        objs=Objects.objects.filter(file_type=type)
    elif category:
        objs=Objects.objects.filter(course_category=category)
    elif year:
        objs=Objects.objects.filter(year=year)
    else:
        objs=Objects.objects.all()
    if coursename and year:
        objs=Objects.objects.filter(coursename=coursename,year=year)
    
    data=[]
    for obj in objs:
        data.append({
            'coursename': obj.coursename,
            'price':obj.price,
            'course_category':obj.course_category,
            'file_type':obj.file_type,
            'thumbnail':obj.thumbnail.url,
            'course_id':obj.course_id,
        })
    
    
    return render(request, 'courses.html',{'page_data':page_data,'data':data})
    
def courses_app(request):
    
    type=request.GET.get('type')
    year=request.GET.get('year')
    category=request.GET.get('course_category')
    
    if type and category and year:
        objs=Objects.objects.filter(file_type=type,year=year,course_category=category)
    elif type and category:
        objs=Objects.objects.filter(file_type=type,course_category=category)
    elif type and year:
        objs=Objects.objects.filter(file_type=type,year=year)
    elif year and category:
        objs=Objects.objects.filter(year=year,course_category=category)
    elif type:
        objs=Objects.objects.filter(file_type=type)
    elif category:
        objs=Objects.objects.filter(course_category=category)
    elif year:
        objs=Objects.objects.filter(year=year)
    else:
        objs=Objects.objects.all()
    
    data=[]
    for obj in objs:
        data.append({
            'coursename': obj.coursename,
            'price':obj.price,
            'course_category':obj.course_category,
            'file_type':obj.file_type,
            'thumbnail':obj.thumbnail.url,
            'course_id':obj.course_id,
        })
    
    
    return JsonResponse({'data':data})
    

def account(request):
    # print(request.user)
    if request.method == 'POST':
        if request.user.is_authenticated:
            name=request.POST.get('name')
            course=request.POST.get('course')
            Phone_number=request.POST.get('Phone_number')
            email=request.POST.get('email')
            Enrollment_Number=request.POST.get('Enrollment_Number')
            Regional_Centre_Code=request.POST.get('Regional_Centre_Code')
            Regional_Centre_Name=request.POST.get('Regional_Centre_Name')
            Study_Centre_Code=request.POST.get('Study_Centre_Code')
            Study_Centre_Name=request.POST.get('Study_Centre_Name')
            session=request.POST.get('Session')
            dob=request.POST.get('dob')
            
            # print(dob)
            
            obj=ExtendedUser.objects.get(user=request.user)
            if obj!=None:
                obj.name=name
                obj.course=course
                obj.Phone_number=Phone_number
                obj.email=email
                obj.Enrollment_Number=Enrollment_Number
                obj.Regional_Centre_Code=Regional_Centre_Code
                obj.Regional_Centre_Name=Regional_Centre_Name
                obj.Study_Centre_Code=Study_Centre_Code
                obj.Study_Centre_Name=Study_Centre_Name
                obj.Session=session
                obj.dob=dob
                obj.save()
        else:
            
            obj_new=ExtendedUser(name=name,course=course,Phone_number=Phone_number,
                                 email=email,Enrollment_Number=Enrollment_Number,
                                 Regional_Centre_Code=Regional_Centre_Code,Regional_Centre_Name=Regional_Centre_Name,
                                 Study_Centre_Code=Study_Centre_Code,Study_Centre_Name=Study_Centre_Name,Session=session,
                                 user=request.user)
            obj_new.save()
            
        obj=ExtendedUser.objects.get(user=request.user)
        
        user_data={
            'name': obj.name,
            'course':obj.course,
            'Phone_number':obj.Phone_number,
            'email':obj.email,
            'Enrollment_Number':obj.Enrollment_Number,
            'Regional_Centre_Code':obj.Regional_Centre_Code,
            'Regional_Centre_Name':obj.Regional_Centre_Name,
            'Study_Centre_Code':obj.Study_Centre_Code,
            'Study_Centre_Name':obj.Study_Centre_Name,
            'Session':obj.Session,
            'userid':obj.id,
            'dob':obj.dob
        }
        if obj.profile_img:
            user_data['profile_img']=obj.profile_img.url
        else:
            user_data['profile_img']=None
        # return render(request, 'account.html',{'user_data':user_data,"alert":"Details Saved Successfully"})
        ses_obj=Session.objects.all()
        sessions=[]
        for s in ses_obj:
            sessions.append({
                'name':s.name,
            })
                
        course_obj=Courses.objects.all()
        courses=[]
        for s in course_obj:
            courses.append({
                'name':s.name,
            })
        return render(request, 'account.html',{'user_data':user_data,'courses':courses,'sessions':sessions})
    else:
        # print(request.user.is_authenticated)
        if request.user.is_authenticated:
            obj=ExtendedUser.objects.get(user=request.user)
            
            user_data={
                'name': obj.name,
                'course':obj.course,
                'Phone_number':obj.Phone_number,
                'email':obj.email,
                'Enrollment_Number':obj.Enrollment_Number,
                'Regional_Centre_Code':obj.Regional_Centre_Code,
                'Regional_Centre_Name':obj.Regional_Centre_Name,
                'Study_Centre_Code':obj.Study_Centre_Code,
                'Study_Centre_Name':obj.Study_Centre_Name,
                'Session':obj.Session,
                'userid':obj.id,
                'dob':obj.dob.strftime("%Y-%m-%d") if obj.dob else ''
            }
            if obj.profile_img:
                user_data['profile_img']=obj.profile_img.url
            else:
                user_data['profile_img']=None
                
            ses_obj=Session.objects.all()
            sessions=[]
            for s in ses_obj:
                sessions.append({
                    'name':s.name,
                })
                 
            course_obj=Courses.objects.all()
            courses=[]
            for s in course_obj:
                courses.append({
                    'name':s.name,
                })
            return render(request, 'account.html',{'user_data':user_data,'courses':courses,'sessions':sessions})
        else:
            return redirect('profile')


def signup(request):
    if request.user.is_authenticated:
        return redirect('account')
    
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        # print(request.POST)

        if password!=confirmpassword or password==None:
            return render(request, 'profile.html',{
                'alert':'Passwords do not match'
            })
        else:
            
            # user_obj=User(username=email,password=password)
            # user_obj.save()
            user_obj=User.objects.create_user(email,email, password)
            user_obj.save()
            user = authenticate(request,username=email, password=password)
            print(user)
            auth.login(request, user)
            extended_obj=ExtendedUser(user=user_obj,email=email)
            extended_obj.save()
            
            return redirect('account')
    else:
        return JsonResponse({'msg':'Invalid Request'})

def demo(request,course_id):
    course=Objects.objects.get(course_id=course_id)
    # return course.free_user_file.url
    return redirect(course.free_user_file.url)


def logout(request):
    # if request.method == 'POST':
    auth.logout(request)
    return redirect('profile')


def updateprofile(request):
    if request.method == 'POST':
        file=request.FILES.get('file')
        # print(file)
        
        # userid=request.POST.get('userid')
        
        obj=ExtendedUser.objects.get(user=request.user)
        obj.profile_img=file
        obj.save()  
        return redirect('account')
        
    else:
        return redirect('account')


def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print(email,password)
        try:
            user = authenticate(request,username=email, password=password)
            # print(user)
            auth.login(request, user)
        except Exception as e:
            return redirect('profile')
            
        # login(user) 
        if user is not None:
            return redirect('index')
        else:
            return redirect('profile')
    else:
        return redirect('profile')
    
    
def profile(request):
    if request.user.is_authenticated:
        return redirect('account')
    return render(request, 'profile.html',{})
        
# def assignments(request):
    
#     course=request.GET.get('course')
#     year=request.GET.get('year')
#     category=request.GET.get('category')
    
#     objs=Objects.objects.filter(file_type='ASSIGNMENT')
    
#     data=[]
#     for obj in objs:
#         data.append({
#             'coursename': obj.coursename,
#             'price':obj.price,
#             'course_category':obj.course_category,
#             'file_type':obj.file_type
#         })
        
#     images=Images.objects.all()
#     img_data=[]
#     for img in images:
#         img_data.append({
#             'img_link':img
#         })
    
#     return render(request, 'assignments.html',{'data':data,'images':img_data})


# @login_required
def cart(request,product_id):
    
    if not request.user.is_authenticated:
        return redirect('profile')
    
    obj=Objects.objects.get(course_id=product_id)
    amount=obj.price
    data = { "amount": amount, "currency": "INR" }
    payment = client.order.create(data=data)
    order_id=payment.get('id')
    ex_user=ExtendedUser.objects.get(user=request.user)
    
    paym_obj=Payment(created_date=datetime.now(),amount=amount,order_id=order_id,object_name=obj,user_paid=ex_user,)
    paym_obj.save()
    order_data={
        'order_id':order_id,
        'amount':int(str(amount)+'00'),
        'name':ex_user.name,
        'email':ex_user.email,  
        }
    
    course=Objects.objects.get(course_id=product_id)
    demo_url=course.free_user_file.url
    
    return render(request, 'cart.html',{"order_data":order_data,"demo_url":demo_url})


import hmac
import hashlib

@csrf_exempt
def callback(request):
    print(request.method)
    if request.method == 'POST':
        razorpay_order_id=request.POST.get('razorpay_order_id')
        razorpay_payment_id=request.POST.get('razorpay_payment_id')
        razorpay_signature=request.POST.get('razorpay_signature')
        # order_id=request.POST.get('order_id')
        # generated_signature = hmac_sha256(order_id + "|" + razorpay_payment_id, RZP_SECRET); 

        paym_obj=Payment.objects.get(user_paid=ExtendedUser.objects.get(user=request.user),order_id=razorpay_order_id)

        generated_signature=hmac.new(RZP_SECRET.encode(), (paym_obj.order_id + "|" + razorpay_payment_id).encode(), hashlib.sha256).hexdigest()
        print(generated_signature,razorpay_signature)
        
        paym_details=client.payment.fetch(razorpay_payment_id)
        
        print(paym_details)
        
        
        # {'id': 'pay_Jq8nGEhdsvtMRB', 'entity': 'payment', 'amount': 200, 'currency': 'INR', 'status': 'captured', 'order_id': 'order_Jq8n7c2VLoWMYy', 'invoice_id': None, 'international': False, 'method': 'netbanking', 'amount_refunded': 0, 'refund_status': None, 'captured': True, 'description': 'Buy Course', 'card_id': None, 'bank': 'YESB', 'wallet': None, 'vpa': None, 'email': 'ajaycool122@gmail.com', 'contact': '+919911693131', 'notes': [], 'fee': 4, 'tax': 0, 'error_code': None, 'error_description': None, 'error_source': None, 'error_step': None, 'error_reason': None, 'acquirer_data': {'bank_transaction_id': '5689393'}, 'created_at': 1657123701}
        if (generated_signature == razorpay_signature) and paym_details['status']=='captured':
            paym_obj.method=paym_details['method']
            paym_obj.status=paym_details['status']
            paym_obj.bank=paym_details['bank']
            paym_obj.wallet=paym_details['wallet']
            paym_obj.vpa=paym_details['vpa']
            paym_obj.bank=paym_details['bank']
            paym_obj.error_code=paym_details['error_code']
            paym_obj.error_description=paym_details['error_description']
            paym_obj.error_source=paym_details['error_source']
            paym_obj.error_step=paym_details['error_step']
            paym_obj.error_reason=paym_details['error_reason']
            paym_obj.save()
            return render(request, 'success.html',{
                'order_id': paym_obj.order_id,
                'amount': paym_obj.amount,
            })
        else:
            paym_obj.method=paym_details['method']
            paym_obj.status=paym_details['status']
            paym_obj.bank=paym_details['bank']
            paym_obj.wallet=paym_details['wallet']
            paym_obj.vpa=paym_details['vpa']
            paym_obj.bank=paym_details['bank']
            paym_obj.error_code=paym_details['error_code']
            paym_obj.error_description=paym_details['error_description']
            paym_obj.error_source=paym_details['error_source']
            paym_obj.error_step=paym_details['error_step']
            paym_obj.error_reason=paym_details['error_reason']
            paym_obj.save()
            return render(request, 'fail.html',{
                'order_id': paym_obj.order_id,
                'amount': paym_obj.amount,
            })

def certificate(request):
    return render(request, 'certificate.html',{})

def contacts(request):
    return render(request, 'contacts.html',{})

def degree(request):
    return render(request, 'degree.html',{})

def diploma(request):
    return render(request, 'diploma.html',{})

def events(request):
    return render(request, 'events.html',{})

def examnotes(request):
    return render(request, 'examnotes.html',{})

def exams(request):
    return render(request, 'exams.html',{})

def pgprogram(request):
    return render(request, 'pgprogram.html',{})

def questionpaper(request):
    return render(request, 'questionpaper.html',{})

def search(request):
    return render(request, 'search.html',{})

def worpro(request):
    return render(request, 'worpro.html',{})
def faqs(request):
    return render(request, 'faqs.html',{})
def tnc(request):
    return render(request, 'tnc.html',{})
def privacypolicy(request):
    return render(request, 'privacy-policy.html',{})


