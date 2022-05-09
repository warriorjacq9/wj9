from django.shortcuts import render, Http404,redirect,HttpResponse
from .forms import DigitalProductForm
from .models import DigitalProduct
from django.core.files.storage import FileSystemStorage

def new_product(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = DigitalProductForm(request.POST, request.FILES)
            if form.is_valid():
                # file is saved
                form.save()
                return redirect('wj9_io:index')
        else:
            form = DigitalProductForm()
        return render(request, 'wj9_io/upload.html', {'form': form})
    else:
        raise Http404()

# Create your views here.
def index(request):
    return render(request, 'wj9_io/index.html')

def products(request):
    products=DigitalProduct.objects.order_by("name")
    context={'products':products}
    return render(request, 'wj9_io/products.html', context)

def product(request, product_id):
    product=DigitalProduct.objects.get(id=product_id)
    filename=product.file.name.split('products/')[1]
    return render(request, 'wj9_io/product.html', {'product':product,'filename':filename})