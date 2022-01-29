from django.shortcuts import render, redirect
from prod.models import categories, products, update_product_price, update_product_quantity

# Create your views here.
def Product(request):
    fetch_caty = categories.objects.all()
    fetch_prod = products.objects.all()
    if request.POST: 
         prod = products(
             name = request.POST['name'],
             categories_id = request.POST['caty'],
             price = request.POST['price'],
             quantity = request.POST['qty'],
             expiry = request.POST['expiry'],
             profit = request.POST['profit'],
             barcode = request.POST['barcode']
         )
         prod.save()
    return render(request, 'prod/manage_prod.html',{'fetch': fetch_caty,'fetch2': fetch_prod})

def Prod_Del(request, id):
    del_prod = products.objects.filter(id=id)
    del_prod.delete()
    return redirect('/ManageProduct')

def Prod_Update(request, id):
    update = products.objects.get(id=id)
    fetch_caty = categories.objects.all()
    return render(request,'prod/update_prod.html', {'update' : update,'fetch': fetch_caty,})

def Prod_Update_Save(request, id):
    name=request.POST['name']
    caty=request.POST['caty']
    old_price=request.POST['old_price']
    old_qty=request.POST['old_qty']
    ids=request.POST['id']
    price=request.POST['price']
    qty=request.POST['qty']
    expiry=request.POST['expiry']
    profit=request.POST['profit']
    barcode=request.POST['barcode']
    prod=products.objects.filter(id=id)
    prod.update(name=name,categories_id=caty,price=price,quantity=qty,expiry=expiry,profit=profit,barcode=barcode)
    if old_price != price:
        if request.POST: 
            rec=update_product_price(
              products_id=ids,
              old_price=old_price,
              new_price=price
            )
            rec.save()
    if old_qty != qty:
        if request.POST: 
            rec=update_product_quantity(
              products_id=ids,
              old_quantity=old_qty,
              new_quantity=qty
            )
            rec.save()
    return redirect('/ManageProduct')

def Prod_Updated_Price(request):
    fetch_caty = update_product_price.objects.all()
    return render(request,'prod/updated_prod_price.html',{'fetch':fetch_caty})

def Prod_Updated_Qty(request):
    fetch_caty = update_product_quantity.objects.all()
    return render(request,'prod/updated_prod_qty.html',{'fetch':fetch_caty})

def Category(request):
    if request.POST: 
         prod=categories(
          name=request.POST['name'], 
         )
         prod.save()
    fetch_caty = categories.objects.all()
    context = {
        'fetch' : fetch_caty
    }
    return render(request,'prod/manage_prod_caty.html', context)

def Caty_Del(request, id):
    del_caty = categories.objects.filter(id=id)
    del_caty.delete()
    return redirect('/ManageCategory')

def Caty_Update(request, id):
    update = categories.objects.get(id=id)
    return render(request,'prod/update_prod_caty.html', {'update' : update})

def Caty_Update_Save(request, id):
    name=request.POST['name']
    dept=categories.objects.filter(id=id)
    dept.update(name=name)
    return redirect('/ManageCategory')

