from django.shortcuts import render

# Create your views here.
def conditonal(request):
    dict={'a' :200,'b':500,'c':600}
    return render(request,'conditonal.html',dict)
    
