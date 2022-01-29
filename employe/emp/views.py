from django.shortcuts import redirect, render
from emp.models import Employee, Designation,Emptren,EPD
from django.contrib import messages
# Create your views here.

def ManagEmp(request):
     if(request.method=='GET' and request.GET.get('method')=='delete' and request.GET.get('id')):
               rec=Employee.objects.filter(id=request.GET.get('id')) 
               rec.delete()

     if(request.method=='GET' and request.GET.get('method')=='edit' and request.GET.get('id')):
               cnt=Employee.objects.filter(id=request.GET.get('id')).get() 
               return render(request, 'emp/update_emp.html',{'row':cnt})
    
     if request.method=='POST':
        if(request.GET.get('method')=='edit'):
             rec=Employee.objects.filter(id=request.GET.get('id'))
             rec.update(
             name=request.POST['name'],
             department=request.POST['department'],
             office=request.POST['office'],
             designation=request.POST['designation'],
             status=request.POST['status'],
                   )
             return redirect('/managemp')
        else:
            data= Employee(
             name=request.POST['name'],
             department=request.POST['department'],
             office=request.POST['office'],
             designation=request.POST['designation'],
             status=request.POST['status'],
             )
            data.save()
            messages.success(request, 'Form submission successful')
     empdata=Employee.objects.all()
          
     return render(request,'emp/manage_emp.html' ,{'emp': empdata})


def ManagDesg(request):
      if(request.method=='GET' and request.GET.get('method')=='delete' and request.GET.get('id')):
               rec=Designation.objects.filter(id=request.GET.get('id')) 
               rec.delete()

      if(request.method=='GET' and request.GET.get('method')=='edit' and request.GET.get('id')):
               cnt=Designation.objects.filter(id=request.GET.get('id')).get() 
               return render(request, 'emp/update_desg.html',{'row':cnt})
    
      if request.method=='POST':
        if(request.GET.get('method')=='edit'):
             rec=Designation.objects.filter(id=request.GET.get('id'))
             rec.update(
             name=request.POST['name'],
             scale=request.POST['scale'],
             ono=request.POST['ono'],
                   )
             return redirect('/updtadesg')
        else:
            data= Designation(
             name=request.POST['name'],
             scale=request.POST['scale'],
             ono=request.POST['ono'],
             )
            data.save()
            messages.success(request, 'Form submission successful')
      desgdata=Designation.objects.all()
          
      return render(request,'emp/manage_desg.html' ,{'desg': desgdata})




def MEmptren(request):
      if(request.method=='GET' and request.GET.get('method')=='delete' and request.GET.get('id')):
               rec=Emptren.objects.filter(id=request.GET.get('id')) 
               rec.delete()

      if(request.method=='GET' and request.GET.get('method')=='edit' and request.GET.get('id')):
               cnt=Emptren.objects.filter(id=request.GET.get('id')).get() 
               return render(request, 'emp/update_emptren.html',{'cnt':cnt})
    
      if request.method=='POST':
        if(request.GET.get('method')=='edit'):
             rec=Emptren.objects.filter(id=request.GET.get('id'))
             rec.update(
             oo=request.POST['oo'],
             no=request.POST['no'],
             ddate=request.POST['ddate'],
                   )
             return redirect('/emptren')
        else:
            data= Emptren(
             oo=request.POST['oo'],
             no=request.POST['no'],
             ddate=request.POST['ddate'],

             )
            data.save()
            messages.success(request, 'Form submission successful')
      desgdata=Emptren.objects.all()
          
      return render(request,'emp/emptren.html' ,{'desg': desgdata})




def epd(request):
      if(request.method=='GET' and request.GET.get('method')=='delete' and request.GET.get('id')):
               rec=EPD.objects.filter(id=request.GET.get('id')) 
               rec.delete()

      if(request.method=='GET' and request.GET.get('method')=='edit' and request.GET.get('id')):
               cnt=EPD.objects.filter(id=request.GET.get('id')).get() 
               return render(request, 'emp/update_epd.html',{'row':cnt})
    
      if request.method=='POST':
        if(request.GET.get('method')=='edit'):
             rec=EPD.objects.filter(id=request.GET.get('id'))
             rec.update(
             cnic=request.POST['cnic'],
             domicle=request.POST['domicle'],
             district=request.POST['district'],
             doj=request.POST['doj'],
             DoB=request.POST['DoB'],
                   )
             return redirect('/epd')
        else:
            data= EPD(
             cnic=request.POST['cnic'],
             domicle=request.POST['domicle'],
             district=request.POST['district'],
             doj=request.POST['doj'],
             DoB=request.POST['DoB'],

             )
            data.save()
            messages.success(request, 'Form submission successful')
      desgdata=EPD.objects.all()
          
      return render(request,'emp/epd.html' ,{'desg': desgdata})