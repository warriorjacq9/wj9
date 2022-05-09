from django.shortcuts import render, Http404
from django.http import HttpResponseRedirect
from .forms import ModelFormWithFileField

def new_product(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ModelFormWithFileField(request.POST, request.FILES)
            if form.is_valid():
                # file is saved
                form.save()
                return HttpResponseRedirect('wj9_io:index')
        else:
            form = ModelFormWithFileField()
        return render(request, 'wj9_io/upload.html', {'form': form})
    else:
        raise Http404()

# Create your views here.
def index(request):
    return render(request, 'wj9_io/index.html')