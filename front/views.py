from django.shortcuts import render,HttpResponse


from django.views.decorators.csrf import csrf_exempt


from .models import Senna


def index(request):
    
    return render(request, 'main/index.html', {})

@csrf_exempt
def graba(request):	
    #file = 'deer.jpg'
    #image = open(file, 'rb')
    #image_read = image.read()
    image_read = request.body
    s = Senna()
    s.img = image_read.decode("utf-8") 
    s.name = "image_read"
    s.desc = "image_read"
    
    s.save()
    
    return HttpResponse("added")
