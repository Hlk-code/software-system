from django.shortcuts import render

# Create your views here.
def index(request):
    content = {
        'aaa':'active',
    }
    return render(request, 'home/base.html',content)
