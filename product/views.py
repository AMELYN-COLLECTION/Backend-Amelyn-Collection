from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Product

# Create your views here.
def manageProduct(request):
    context = {
        'product': Product.objects.all()
    }
    return render(request, 'manage_product.html', context)

def createProduct(request):
    
    if request.method == "POST":
        image = request.FILES['imageProduct']

        name = request.POST.get('nameProduct')
        price = request.POST.get('priceProduct')
        desc = request.POST.get('descProduct')
        size = request.POST.get('sizeProduct')
        stock = request.POST.get('stockProduct')
        
        try:
            Product.objects.create(imageProduct=image, nameProduct=name, descProduct=desc, sizeProduct=size, stockProduct=stock, priceProduct=int(
                price))

            messages.success(request, 'Success menambah menu baru')
        except:
            messages.error(request, 'Failed menambah menu baru')

    return redirect('product:manage-product')

def updateProduct(request):
    if request.method == "POST":
        productId = request.POST.get('id')
        image = request.FILES['imageProduct']
        name = request.POST.get('nameProduct')
        price = request.POST.get('priceProduct')
        desc = request.POST.get('descProduct')
        size = request.POST.get('sizeProduct')
        stock = request.POST.get('stockProduct')
        
        product_obj = Product.objects.get(id=productId)
        product_obj.imageProduct = image
        product_obj.nameProduct = name
        product_obj.descProduct = desc
        product_obj.priceProduct = int(price)
        product_obj.sizeProduct = size
        product_obj.stockProduct = stock
        
        try:
            product_obj.save()

            messages.success(request, 'Success menambah menu baru')
        except:
            messages.error(request, 'Failed menambah menu baru')
            print(Exception)
    return redirect('product:manage-product')

def deleteProduct(request):
    if request.method == "POST":
        try:
            
        
            Product.objects.filter(id=request.POST.get('id')).delete()
            messages.success(request, 'Success delete menu')
        except:
            messages.error(request, 'Failed delete menu')
    return redirect('product:manage-product')
    