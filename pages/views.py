from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def landing(request):
    return render(request, 'landingpage.html', {})

@login_required()
def resources(request):
    return render(request, 'resources.html', {})

def error_404(request, exception):
    return render(request, '404.html')