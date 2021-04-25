from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def info(request):
    if request.method =="POST":
        name = request.POST["name"]
        location = request.POST["location"]
        language = request.POST["language"]
        desc = request.POST["desc"]
        gender = request.POST["gender"]
        level = request.POST["level"]
        request.session['name'] = name
        request.session['location'] = location
        request.session['language'] = language
        request.session['desc'] = desc
        request.session['gender'] = gender
        request.session['level'] = level
    return redirect('/show')
    
def show(request):
    return render(request,'index.html')
    #return HttpResponse(request)