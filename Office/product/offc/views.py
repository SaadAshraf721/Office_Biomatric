from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader 
from .models import ofice,department,adoo
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def office(request):  
    return render(request,'offc/office.html')

def add_office(request):  
    try:
      if request.method =='POST':
        name=request.POST['name']
        check=ofice.objects.get(nam=name)
        if check:
              messages.success(request,'Record alredy exist!')
              return redirect('/addoffice')
    except ObjectDoesNotExist:
      if request.method =='POST':
          name=request.POST['name']
          loc=request.POST['loc']
          level=request.POST['level']
          rec = ofice(
              nam=name,
              location=loc,
              level=level
          )
          rec.save()
          if rec:
              messages.success(request,'Record added successfully')
              return redirect('/addoffice')
          else:
              messages.warning(request,'Record not added !')
              return redirect('/addoffice')
    fetch_dept=ofice.objects.all()
    return render(request,'offc/add_office.html',{'ofice':fetch_dept})

def add_department(request):  
    try:
      if request.method =='POST':
        name=request.POST['department']
        check=department.objects.get(name=name)
        if check:
              messages.success(request,'Record alredy exist!')
              return redirect('/AddDepartment')
    except ObjectDoesNotExist:
      if request.method =='POST':
          name=request.POST['department']
          rec = department(
              name=name
          )
          rec.save()
          if rec:
              messages.success(request,'Record added successfully')
              return redirect('/AddDepartment')
          else:
              messages.warning(request,'Record not added !')
              return redirect('/AddDepartment')
    fetch_dept=department.objects.all()
    return render(request,'offc/add_dept.html',{'dept':fetch_dept})

def del_dept(request, id):
    del_dept=department.objects.get(id=id)
    del_dept.delete()
    return redirect('/AddDepartment')

def del_ofc(request, id):
    del_dept=ofice.objects.get(id=id)
    del_dept.delete()
    return redirect('/addoffice')

def ado(request):
    try:
      if request.method =='POST':
        oi=request.POST['oi']
        di=request.POST['di']
        check=adoo.objects.get(oi_id=oi,di_id=di)
        if check:
              messages.success(request,'Record alredy exist!')
              return redirect('/ADO')
    except ObjectDoesNotExist:
      if request.method =='POST':
          oi=request.POST['oi']
          di=request.POST['di']
          rec = adoo(
            oi_id=oi,di_id=di
          )
          rec.save()
          if rec:
              messages.success(request,'Record added successfully')
              return redirect('/ADO')
          else:
              messages.warning(request,'Record not added !')
              return redirect('/ADO')
    ofc=ofice.objects.all()
    dept=department.objects.all()
    ado=adoo.objects.filter()
    return render(request,'offc/ado.html',{'dept':dept,'ofc':ofc,'ado':ado})

def del_ado(request, id):
    del_dept=adoo.objects.get(id=id)
    del_dept.delete()
    return redirect('/ADO')

def update_dept(request, id):
    dept=department.objects.get(id=id)
    return render(request,'offc/update_dept.html',{'dpt':dept})

def update_dept_save(request, id):
    name=request.POST['department']
    dept=department.objects.filter(id=id)
    dept.update(name=name)
    return redirect('/AddDepartment')

def update_ofc(request, id):
    dept=ofice.objects.get(id=id)
    return render(request,'offc/update_ofc.html',{'dpt':dept})

def update_ofc_save(request, id):
    name=request.POST['name']
    loc=request.POST['loc']
    level=request.POST['level']
    dept=ofice.objects.filter(id=id)
    dept.update(nam=name,location=loc,level=level)
    return redirect('/addoffice')

def update_ado(request, id):
    dept=adoo.objects.get(id=id)
    ofc=ofice.objects.all()
    dp=department.objects.all()
    return render(request,'offc/update_ado.html',{'dpt':dept,'dp':dp,'ofc':ofc})

def update_ado_save(request, id):
    oi=request.POST['oi']
    di=request.POST['di']
    dept=adoo.objects.filter(id=id)
    dept.update(oi_id=oi,di_id=di)
    return redirect('/ADO')