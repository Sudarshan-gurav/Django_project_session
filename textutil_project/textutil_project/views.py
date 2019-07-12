# i have create this file - sudashan
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('''hello page''')
    # d = {'name' : 'sudarshan', 'age':24}
    return render(request,'index.html')
 
def remove_puch(request):
    # get the text from html
    return HttpResponse('''<h4>remove punctuations </h4> <a href="/"> Back </a>''')

def capfirst(request):
    return HttpResponse("capital each letter <br ><a href='/'> Home </a>")

def newlineremove(request):
    return HttpResponse(" new line remove <br ><a href='/'> Home </a> ")

def spaceremove(request):
    return HttpResponse(" space remove <br ><a href='/'> Home </a>")

def charcounter(request):
    return HttpResponse("charecter counter <br ><a href='/'> Home </a>")

def analyze(request):
    djtext = request.GET.get('text','default')
    remove_puc = request.GET.get('removepuch','off')
    puctuations = '''~!@$%^&*()_+|:"<>?`-=][';/.,]'''
    analyzed = ""
    for char in djtext:
        if char not in puctuations:
            analyzed = analyzed + char
        param = {'purpose': 'Remove punctuation','analyze_text': analyzed }
    return render(request,'analyze.html',param)



