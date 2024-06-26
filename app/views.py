from django.shortcuts import render

# Create your views here.
def jinga_print(request):
    d={'name':'chandu','age':'secrete'}
    return render(request,'jinja_print.html',context=d)