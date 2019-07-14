from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,'home.html')

def auth(request):
    u_id = request.GET.get('userid','default')
    pwd = request.GET.get('pwd','default')

    if u_id =='shree' and pwd == 'admin':
        return render(request,'auth.html') 
    else:
        return HttpResponse('''please try one more time <a href='/'> back to login page </a>''')
