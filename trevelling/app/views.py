from django.shortcuts import render

def home(req):
    return render(req,'app/index.html')
def about(req):
    return render(req,'app/about.html')
def  Contact(req):
    return render(req,'app/Contact.html')
def  Gallry(req):
    return render(req,'app/Gallry.html')



# Create your views here.
