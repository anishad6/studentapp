from django.shortcuts import render , redirect
from studentapp.models import  Students


# Create your views here.
def home(request):
    data=Students.objects.all()
    # data = Department.objects.filter(status=True)
    context={}
    context['students']=data
    return render(request, "index.html",context)

def addStudent(request):
    if request.method =="GET":
        return render(request,'add.html')
    else:
        # student= Students.objects.all()
        n=request.POST["name"]
        e=request.POST["email"]
        num=request.POST["phone_number"]
        p=request.POST["per"]
        b=request.POST["branch"]
        a=request.POST["address"]
        s=Students.objects.create(name=n,email=e,phone_number=num,per=p,branch=b,address=a)
        s.save()
        return redirect('/')
    
def update(request,studentsid):
    if request.method =="GET":
        student=Students.objects.get(id=studentsid)
        context={}
        context["students"]=student
        return render(request,'update.html',context)
    else:
        student=Students.objects.filter(id=studentsid)
        name=request.POST["name"]
        email=request.POST["email"]
        number=request.POST["phone_number"]
        per=request.POST["per"]
        branch=request.POST["branch"]
        address=request.POST["address"]
        student.update(name=name,email=email,phone_number=number,per=per,branch=branch,address=address)
        return redirect('/')
    
def delete(request,studentsid):
    student=Students.objects.filter(id=studentsid)
    student.delete()
    return redirect('/')

