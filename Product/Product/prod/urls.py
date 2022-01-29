from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from prod import views

urlpatterns = [
    path('ManageProduct', views.Product),
    path('ProductDel/<int:id>', views.Prod_Del),
    path('ProductUpdate/<int:id>', views.Prod_Update),
    path('ProductUpdateSave/<int:id>', views.Prod_Update_Save),
    path('ProductUpdatedPrice', views.Prod_Updated_Price),
    path('ProductUpdatedQty', views.Prod_Updated_Qty),
    path('ManageCategory', views.Category),
    path('CategoryDel/<int:id>', views.Caty_Del),
    path('CategoryUpdate/<int:id>', views.Caty_Update),
    path('CategoryUpdateSave/<int:id>', views.Caty_Update_Save),
]