from django.shortcuts import render
from .models import Form

# Create your views here.
def index(request):
    return render(request,'form/index.html')


def form(request):
    
    if request.method =='POST':
        firstname_r=request.POST.get('firstname')
        lastname_r=request.POST.get('lastname')
        message_r=request.POST.get('message')
        email_r = request.POST.get('email')

        c=Form(firstname=firstname_r,lastname=lastname_r,message=message_r,email=email_r)
        c.save()

        return render(request,'form/form.html')
    else:
        return render(request,'form/form.html')
