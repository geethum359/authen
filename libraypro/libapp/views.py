
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from libapp.forms import CustomUserCreationForm
# from libapp.models import CustomUser
from django.http import HttpResponse
# from libapp.forms import employeeForm
from django.contrib.auth import authenticate,login,logout
from libapp.models import register
from libapp.forms import reisterform
# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')

def register(request):
    if(request.method=="POST"):
        first_name= request.POST['fn']
        last_name= request.POST['ln']
        gen= request.POST['g']
        dob= request.POST['d']
        email= request.POST['e']
        phno= request.POST['ph']
        addrs= request.POST['a']
        u =register.objects.create(First_Name=first_name,Last_Name=last_name,Gender=gen,Date_Of_Brith=dob,Your_Email=email,Phone_Number=phno,Address=addrs,)
        u.save()
        return home(request)
    return render(request,'register.html')
    
def user_login1(request):
    if(request.method=="POST"):
        name = request.POST['n']
        password = request.POST['p']
        user =authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse('invalid ... no user found')
    return render(request,'login1.html')
def user_logout1(request):
    logout(request)
    return user_login1(request)


def signup1(request):
    form=CustomUserCreationForm()
    if(request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request,'signup1.html',{"form":form})









# def view(request):
#     v=employee.objects.all()
#     return render(request,'view.html',{"s":v})
# def  addform(request):
#     form=employeeForm()
#     if request.method=='POST':
#         form=employeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return view(request)
#     return render(request,'addform.html',{'form':form})
# def delete_emp(request,p):
#     s=employee.objects.get(pk=p)
#     s.delete()
#     return view(request)
# def edit_emp(request,p):
#     d=employee.objects.get(pk=p)
#     form=employeeForm(instance=d)
#     if(request.method=='POST'):
#         form=employeeForm(request.POST,instance=d)
#         if(form.is_valid()):
#             form.save()
#             return view(request)
#     return render(request,'addform.html',{'form':form})
# def data(request,p):
#     k=employee.objects.get(pk=p)
#     return render(request,'view_data.html',{'a':k})

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
# from django.shortcuts import render, get_object_or_404
 
# from .models import post, PostImage
 
# def blog_view(request):
#     posts = post.objects.all()
#     return render(request, 'blog.html', {'posts':posts})
 
# def detail_view(request, id):
#     post = get_object_or_404(post, id=id)
#     photos = PostImage.objects.filter(post=post)
#     return render(request, 'detail.html', {
#         'post':post,
#         'photos':photos
#     })