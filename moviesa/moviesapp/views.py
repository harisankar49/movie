from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movieform
# Create your views here.
#def index(request):
    #movie_list=movie.objects.all()
    #context={"movies":movie_list}

    #return render(request,'index.html',context)
#def detail(request,movie_id):
    #return HttpResponse("This is movie id %s" %movie_id)
def detail(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{"lst":mov})
def bindex(request):
    movie_list=movie.objects.all()
    context={"movies":movie_list}

    return render(request, 'bindex.html', context)
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        #movie is the database name
        mov.save()
    return render(request,'add.html')
def update(request, id):


    mov=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('bindex/')

    return render(request,'edit.html',{'form':form,'movie':mov})
def delete(request,id):
    if request.method=='POST':
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('bindex/')
    return render(request,'delete.html')
