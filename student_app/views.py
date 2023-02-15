from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from student_app.forms import Login_Form, StudentRegisterForm, AdminRegisterForm, MarkForm
from student_app.models import StudentRegister, Mark


# Create your views here.

def index(request):
    return render(request,"index.html")

def indexx(request):
    return render(request,"indexx.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_adm:
                return redirect("adminbase")
            if user.is_student:
                return redirect("studentbase")

        else:
            messages.info(request,"Invalid credentials")
    return render(request,"login.html")



###############ADMIN#############

def adminbase(requset):
    return render(requset,"adm12/admin base.html")

def students_data(request):
    data = StudentRegister.objects.all()
    print(data)
    return render(request,"adm12/student_data.html",{'data':data})

def admin_register(request):
    form1 = Login_Form()
    print(form1)
    form2 = StudentRegisterForm()
    if request.method == "POST":
        form1 = Login_Form(request.POST)
        form2 = AdminRegisterForm(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_adm = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("login_page")
    return render(request,"adm12/admin_register.html",{'form1':form1,'form2':form2})


def add_mark(request):
    form = MarkForm()
    if request.method =='POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_mark")
    return render(request,'adm12/add_mark.html',{'form':form})



def view_mark(request):
    data = Mark.objects.all()
    return render(request,'adm12/view_mark.html',{'data':data})

def edit_view_mark(request,id):

        a = Mark.objects.get(id=id)
        form = MarkForm(instance=a)
        if request.method == 'POST':
            form = MarkForm(request.POST, instance=a)
            if form.is_valid():
                form.save()
                return redirect("view_mark")

        return render(request, "adm12/edit_view_mark.html", {'form': form})




###################STUDENT##############


def studentbase(request):
    return render(request,"student/studentbase.html")

def student_register(request):
    form1 = Login_Form()
    print(form1)
    form2 = StudentRegisterForm()
    if request.method == "POST":
        form1 = Login_Form(request.POST)
        form2 = StudentRegisterForm(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_student = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("login_page")
    return render(request,"student/student_register.html",{'form1':form1,'form2':form2})


# def validate_file_size(value):
#     filesize = value.size
#
#     if filesize > 10485760:
#         raise ValidationError("The maximum file size that can be uploaded is 10MB")
#     else:
#         return value

def personal_details(request):
    data = StudentRegister.objects.all()
    return render(request,"student/personal details.html",{'data':data})

def edit_personal_details(request, id):

        a = StudentRegister.objects.get(id=id)
        form = StudentRegisterForm(instance=a)
        if request.method == 'POST':
            form = StudentRegisterForm(request.POST, instance=a)
            if form.is_valid():
                form.save()
                return redirect("personal_details")

        return render(request, "student/edit_personal_details.html", {'form': form})
