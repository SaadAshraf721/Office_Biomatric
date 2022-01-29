from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from offc import views
urlpatterns = [
    path('addoffice', views.add_office),
    path('DeptOfice/<int:id>', views.del_ofc),
    path('AddDepartment', views.add_department),
    path('DeptDel/<int:id>', views.del_dept),
    path('ADO', views.ado),
    path('ADODel/<int:id>', views.del_ado),
    path('UpdateDept/<int:id>', views.update_dept),
    path('UpdateDeptSave/<int:id>', views.update_dept_save),
    path('UpdateOffice/<int:id>', views.update_ofc),
    path('UpdateOfcSave/<int:id>', views.update_ofc_save),
    path('UpdateAdo/<int:id>', views.update_ado),
    path('UpdateADOSave/<int:id>', views.update_ado_save),





]
