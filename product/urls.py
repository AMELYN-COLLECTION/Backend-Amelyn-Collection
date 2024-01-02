from django.urls import path

from . import views

urlpatterns = [
    path('manage-product/', views.manageProduct, name="manage-product"),
    path('create-product/', views.createProduct, name="create-product"),
    path('update-product/', views.updateProduct, name="update-product"),
    path('delete-product/', views.deleteProduct, name="delete-product"),
]