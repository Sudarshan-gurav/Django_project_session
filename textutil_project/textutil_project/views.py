# i have create this file - sudashan
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello")


def about(request):
    return HttpResponse('about')

