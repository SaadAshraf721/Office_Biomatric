
from django.urls import path
from .views import ManagEmp,ManagDesg,MEmptren, epd

urlpatterns = [
    path('managemp/',ManagEmp),
    path('updtadesg/',ManagDesg),
    path('emptren/',MEmptren),
    path('epd/',epd),
   
]
